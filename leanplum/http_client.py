import textwrap

from leanplum import errors

try:
    import requests
except ImportError:
    requests = None


def new_default_http_client(*args, **kwargs):
    # can cache client as lp.default_http_client
    if requests:
        impl = RequestsClient
    else:
        impl = HttpClient
    # other impls
    return impl(*args, **kwargs)


class HttpClient(object):
    def request(self, method, url, headers, post_data=None):
        raise NotImplementedError(
            'HTTPClient subclasses must implement `request`')


class RequestsClient(HttpClient):
    name = 'requests'

    def __init__(self, timeout=60, session=None, **kwargs):
        super(RequestsClient, self).__init__(**kwargs)
        self._timeout = timeout
        self._session = session or requests.Session()

    def request(self, method, url, headers, post_data=None):
        kwargs = {}

        try:
            try:
                # LEAKED CONNECTION bug
                # https://github.com/stripe/stripe-python/issues/432
                result = self._session.request(method,
                                               url,
                                               headers=headers,
                                               data=post_data,
                                               timeout=self._timeout,
                                               **kwargs)
            except TypeError as e:
                raise TypeError(
                    'Warning: It looks like your installed version of the '
                    '"requests" library is not compatible with Stripe\'s '
                    'usage thereof. (HINT: The most likely cause is that '
                    'your "requests" library is out of date. You can fix '
                    'that by running "pip install -U requests".) The '
                    'underlying error was: %s' % (e,))

            # This causes the content to actually be read, which could cause
            # e.g. a socket timeout.
            # are susceptible to the same and should be updated.
            content = result.content
            status_code = result.status_code
        except Exception as e:
            # Would catch just requests.exceptions.RequestException, but can
            # also raise ValueError, RuntimeError, etc.
            self._handle_request_error(e)
        return content, status_code, result.headers

    def _handle_request_error(self, e):
        if isinstance(e, requests.exceptions.RequestException):
            msg = "Unexpected error in Requests"
            err = "%s: %s" % (type(e).__name__, str(e))
        else:
            msg = "Unexpected error communicating with Leanplum"
            err = "A %s was raised" % (type(e).__name__,)
            if str(e):
                err += " with error message %s" % (str(e),)
            else:
                err += " with no error message"
        msg = textwrap.fill(msg) + "\n\n(Network error: %s)" % (err,)
        raise errors.ConnectionError(msg)
