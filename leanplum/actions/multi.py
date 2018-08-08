from leanplum.actions.abstract import BaseResource

__all__ = ['Multi']


class Multi(BaseResource):

    def batch(self, data):
        """

        :param list, data:
        :return:
        """

        for action in data:
            pass

        return self._client.request('POST', 'multi', data)
