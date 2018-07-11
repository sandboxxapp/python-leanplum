from leanplum.actions.abstract import BaseResource


class Admin(BaseResource):

    def delete_user(self, user_id):
        if not user_id:
            raise ValueError("A user_id must be supplied to delete a user")

        raise NotImplementedError("admin.delete_user is not fully implemented")
