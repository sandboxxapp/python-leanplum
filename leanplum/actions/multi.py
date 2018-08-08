from leanplum.actions.abstract import BaseResource

__all__ = ['Multi']


class Multi(BaseResource):

    def batch(self, time, data):
        """

        :param int time: REQUIRED The time at which the request was issued (UNIX time).
        :param list, data: REQUIRED A list of API methods to execute. All methods must be for the same app referred to
        by the appId parameter. Each data object must include the required arguments for its API action.
        :return: The response from Leanplum api
        """

        if not isinstance(data, list):
            raise TypeError("data should be type list, got {}".format(type(data)))

        return self._client.request_multi('POST', 'multi', time, data)
