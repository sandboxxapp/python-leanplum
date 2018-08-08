from collections import OrderedDict

import leanplum
from leanplum.requestor import ApiRequestor


class Client(object):

    def __init__(self, app_id=None, client_key=None, api_version=None):
        self._app_id = app_id
        self._client_key = client_key
        self._api_version = api_version or leanplum.api_version
        self._requestor = ApiRequestor()

    @property
    def users(self):
        from leanplum.actions.users import Users
        return Users(self)

    @property
    def admin(self):
        from leanplum.actions.admin import Admin
        return Admin(self)

    @property
    def multi(self):
        from leanplum.actions.multi import Multi
        return Multi(self)

    def request(self, method, action, params):
        params = self._format_params(action, **params)
        return self._requestor.request(method, params)

    def _format_params(self, action, **params):
        params = OrderedDict(action=action,
                             appId=self._app_id,
                             clientKey=self._client_key,
                             apiVersion=self._api_version,
                             **params)
        return params
