from __future__ import absolute_import, division, print_function


class LeanplumError(Exception):
    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None, headers=None, code=None):
        super(LeanplumError, self).__init__(message)

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
        self.code = code


class APIError(LeanplumError):
    """
    Generic API error, usually a code 200 but with a response.error.message
    """
    pass


class ConnectionError(LeanplumError):
    """
    An error representing transport-layer problems, usually in the http client.
    E.g. RequestsClient times out, then we will raise a ConnectionError
    """
    pass


class BadRequestError(LeanplumError):
    """
    Represents a 400 Bad Request where a parameter or parameters were not supplied
    E.g. appId, clientKey, or any other required param (userId, deviceId, etc) is missing
    """
    pass


class WrongValueError(LeanplumError):
    """
    Represents a 404 Not Found request failure where an id wasn't found
    E.g. the appId is bad/wrong

    Note: this is not used in the case that a request was accepted (200) but not actioned upon due to a bad
    userId or deviceId.  In those cases, the response will return a 200, success=true but with a warning
    that the request was skipped (I wish this behavior was different).
    """
    pass


class InvalidKeyError(LeanplumError):
    """
    We've seen issues around a bad client key (using the debugKey instead of croKey, etc)
    This represents a 403 Forbidden http status
    """
    pass
