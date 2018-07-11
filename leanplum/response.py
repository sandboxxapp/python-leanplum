# TODO: in requestor.interpret_response, we can objectify the response


class ResponseList(object):
    """
    {
        "response": [{
            "success" : true,
            "warning": "optional warning message",
            "error": "optional error message"
        }, ...]
    }
    """

    def __init__(self, code, responses):
        self._code = code
        self._responses = []
        if type(responses) is list:
            for item in responses:
                self._responses.append(Response(item))
        else:
            raise TypeError("Leanplum ResponseList needs a list")

    @property
    def code(self):
        return int(self._code)

    @property
    def responses(self):
        return self._responses

    def get_item(self, index=0):
        return self._responses[index] if index else None


class Response(object):

    class MessageBody(object):

        def __init__(self, json_dict=None):
            if json_dict:
                self._message = json_dict.get("message") or None
            else:
                self._message = None

        @property
        def message(self):
            return self._message

    def __init__(self, json_dict):
        self._success = json_dict.get("success")
        self._warning = self.MessageBody(json_dict.get("warning"))
        self._error = self.MessageBody(json_dict.get("error"))

    @property
    def success(self):
        return self._success

    @property
    def warning(self):
        return self._warning

    @property
    def error(self):
        return self._error
