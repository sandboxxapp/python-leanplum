from leanplum.actions.abstract import BaseResource

__all__ = ['Admin']


class Admin(BaseResource):

    def delete_user(self, user_id, full_erasure=False):
        """
        https://docs.leanplum.com/reference#post_api-action-setuserattributes

        :param user_id: REQUIRED The current user ID
        :param bool full_erasure:
        :return: If True, deletes all session and analytics data for the selected user (set True
        for GDPR-related deletion requests)
        """
        if not user_id:
            raise ValueError("user_id is a required field")

        params = {
            "userId": user_id,
            "fullErasure": full_erasure
        }

        self._client.request('POST', 'deleteUser', params)

    def export_user(self, user_id):
        """
        https://docs.leanplum.com/reference#get_api-action-exportuser

        * The Export Key is used in place of the regular client_key

        :param user_id: REQUIRED The current user ID
        :return: Retrieves attributes for the current user. This method requires your data export API clientKey.
        """
        if not user_id:
            raise ValueError("user_id is a required field")

        params = {
            "userId": user_id
        }

        return self._client.request('GET', 'exportUser', params)
