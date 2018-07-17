from leanplum.actions.abstract import BaseResource


class Admin(BaseResource):

    def delete_user(self, user_id, full_erasure=False):
        if not user_id:
            raise ValueError("A user_id must be supplied to delete a user")

        params = {
            "userId": user_id,
            "fullErasure": full_erasure
        }

        self._client.request('POST', 'deleteUser', params)
