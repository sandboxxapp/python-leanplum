import json
import platform
import urllib

import leanplum
from leanplum import errors, http_client, logger


class ApiRequestor(object):

    def __init__(self, client=None, api_base=None):
        self.api_base = api_base or leanplum.api_base
        self._client = client or leanplum.default_http_client or http_client.new_default_http_client()
        self.logger = leanplum.default_logger or logger.new_default_logger()

    def request(self, method, params=None):
        rbody, rcode, rheaders = self._request_raw(method.lower(), self.api_base, params)
        return self.interpret_response(rbody, rcode, rheaders)

    def _request_raw(self, method, url, params=None):
        """
        Mechanism for issuing an API call
        :type params: dict
        """

        # apply headers
        headers = self._request_headers(method)

        # put data in query params for GET and body for POST
        abs_url = url
        post_data = None
        if method == 'get':
            abs_url = "{}&{}".format(url, self._encode_query_params(params))
        elif method == 'post':
            if headers['Content-Type'] == 'application/json':
                post_data = json.dumps(params)
            else:
                post_data = params

        self.logger.debug("{}\t=> {}".format(method.upper(), abs_url))
        if post_data:
            self.logger.debug("POST\t=> {}".format(post_data))
        elif params:
            self.logger.debug("GET\t=> {}".format(params))

        rbody, rcode, rheaders = self._client.request(method, abs_url, headers, post_data)

        self.logger.debug("{}\t<= {} {}".format(method.upper(), rcode, rbody))

        return rbody, rcode, rheaders

    def interpret_response(self, body, code, headers):
        # HTTP responses (error or success) always make it to here.
        # Errors in the transport layer are raised as exceptions before they reach here

        body = json.loads(body)  # slap it in a dictionary

        response = body.get("response")[0]  # it's in the first index TODO: Support multi blahhhhh
        success = response.get("success")

        if code == 200 and success:
            # coerce type?
            pass
        elif code == 200 and not success:
            # handle one of warning or error
            pass
        else:
            self.handle_error_response(body, code, response, headers)

        # TODO: method should return a Response object
        return body

    def handle_error_response(self, rbody, rcode, resp, rheaders):
        try:
            error_data = resp['error']
        except (KeyError, TypeError):
            raise errors.APIError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (rbody, rcode),
                rbody, rcode, resp)

        err = None

        if err is None:
            err = self.specific_api_error(
                rbody, rcode, resp, rheaders, error_data)

        raise err

    def specific_api_error(self, rbody, rcode, response, rheaders, error_data):
        message = error_data['message']

        if rcode == 400:
            return errors.BadRequestError(message, rbody, rcode)
        elif rcode == 403:
            return errors.InvalidKeyError(message, rbody, rcode)
        elif rcode == 404:
            return errors.WrongValueError(message, rbody, rcode)
        elif rcode == 500:
            return errors.APIError(message, rbody, rcode)
        else:
            return errors.APIError(message, rbody, rcode)

    def _request_headers(self, method):
        user_agent = 'Leanplum/v1 PythonBindings/%s' % (leanplum.__version__,)

        ua = {
            'bindings_version': leanplum.__version__,
            'lang': 'python',
            'publisher': 'sandboxx/leanplum',
            'httplib': self._client.name,
        }
        for attr, func in [['lang_version', platform.python_version],
                           ['platform', platform.platform],
                           ['uname', lambda: ' '.join(platform.uname())]]:
            try:
                val = func()
            except Exception as e:
                val = "!! %s" % (e,)
            ua[attr] = val

        headers = {
            'X-Leanplum-Client-User-Agent': json.dumps(ua),
            'User-Agent': user_agent,
        }

        if method == 'post':
            headers['Content-Type'] = 'application/json'

        return headers

    def _get_authorizations(self, app_id, api_key):
        return {
            "appId": app_id,
            "clientKey": api_key,
            "apiVersion": self.api_version
        }

    @staticmethod
    def _encode_query_params(params):
        return urllib.urlencode(params)
