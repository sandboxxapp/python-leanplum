from leanplum.actions.abstract import BaseResource
from leanplum.actions import disposition

__all__ = ['Users']


class Users(BaseResource):

    def advance(self, user_id, state, info=None, params=None, create_disposition=disposition.CREATE_NEVER):
        """
        https://docs.leanplum.com/reference#post_api-action-advance

        :param user_id: REQUIRED The current user ID
        :param str, state: REQUIRED The name of the state
        :param str info: Any info attached to the state.
        :param dict params: A flat object of parameters as key-value pairs.
        :param str create_disposition: The policy that determines whether users are created by the API. Default: CreateNever
        :return: The response from Leanplum api
        """

        if not user_id:
            raise ValueError("user_id is a required field")
        if not state:
            raise ValueError("state is a required field")
        if not isinstance(state, basestring):
            raise TypeError("state should be type string, got {}".format(type(state)))

        if params and type(params) is not dict:
            raise TypeError("params must be None or type dict")

        params = {
            "userId": user_id,
            "state": state,
            "info": info,
            "params": params,
            "createDisposition": create_disposition
        }
        return self._client.request('POST', 'advance', params)

    def track(self, user_id, event, value=None, info=None, time=None, params=None, create_disposition=disposition.CREATE_NEVER):
        """
        https://docs.leanplum.com/reference#post_api-action-track

        :param user_id: REQUIRED The current user ID
        :param str event: REQUIRED The name of the event
        :param float value: The event value.  For "Purchase" events, the would be the purchase price
        :param str info: Any info attached to the event
        :param int time: The UNIX timestamp for when the event occurred, provide to override current time
        :param dict params: A flat object of parameters as key-value pairs.
        :param str create_disposition: The policy that determines whether users are created by the API. Default: CreateNever
        :return: The response from Leanplum api
        """

        if not user_id:
            raise ValueError("user_id is a required field")
        if not event:
            raise ValueError("event is a required field")
        if not isinstance(event, basestring):
            raise TypeError("event should be type string, got {}".format(type(event)))

        if params and type(params) is not dict:
            raise TypeError("params must be None or type dict")

        params = {
            "userId": user_id,
            "event": event,
            "value": value,
            "info": info,
            "time": time,
            "params": params,
            "createDisposition": create_disposition
        }
        return self._client.request('POST', 'track', params)

    def set_user_attributes(self, user_id, attributes, attributes_to_add=None, attributes_to_remove=None, create_disposition=disposition.CREATE_NEVER):
        """
        https://docs.leanplum.com/reference#post_api-action-setuserattributes

        :param user_id: REQUIRED The current user ID
        :param dict attributes: A map of user attributes as key-value pairs.
        :param dict attributes_to_remove: A map of values to add to existing user attribute sets.
        :param dict attributes_to_add: A map of values to remove from existing user attribute sets.
        :param str create_disposition: The policy that determines whether users are created by the API. Default: CreateNever
        :return: The response from Leanplum api
        """

        if not user_id:
            raise ValueError("user_id is a required field")

        if type(attributes) is not dict:
            raise ValueError("SetUserAttributes attributes param must be of type dict")

        params = {
            "userId": user_id,
            "userAttributes": attributes,
            "userAttributeValuesToAdd": attributes_to_add,
            "userAttributeValuesToRemove": attributes_to_remove,
            "createDisposition": create_disposition
        }
        return self._client.request('POST', 'setUserAttributes', params)

    def set_new_user_id(self, user_id, new_user_id):
        """
        https://docs.leanplum.com/v1/reference#post_api-action-setuserattributes

        This call can have a few different effects:
        - Login: If the current user has no user ID and the user given by newUserId already exists,
        the current and existing user profiles will be merged, and the current profile will be deleted.

        - Register: If there is no current user ID and the user given by newUserId does not exist, the current user
        will be simply assigned newUserId as its user ID.

        - Switch user: If the current user has a user ID, the current session will be ended and a new session will be
        started with the user given by newUserId. A user with newUserId will be created if one does not already exist.

        :param user_id: REQUIRED The current user ID
        :param new_user_id: REQUIRED The new user ID
        :return: The response from Leanplum api
        """

        if not user_id:
            raise ValueError("user_id is a required field")
        if not new_user_id:
            raise ValueError("new_user_id is a required field")

        params = {
            "userId": user_id,
            "newUserId": new_user_id
        }

        return self._client.request('POST', 'setUserAttributes', params)

    def increment_user_attribute(self, user_id, attribute, incr=1, create_disposition=disposition.CREATE_NEVER):
        """
        https://docs.leanplum.com/reference#post_api-action-setuserattributes

        :param user_id: REQUIRED The current user ID
        :param str attribute: REQUIRED The name of the attribute to increment
        :param int incr: The value to increment by.  Default is 1
        :param str create_disposition:The policy that determines whether users are created by the API. Default: CreateNever
        :return: The response from Leanplum api
        """

        if not user_id:
            raise ValueError("user_id is a required field")
        if not attribute:
            raise ValueError("attribute is a required field")
        if not isinstance(attribute, basestring):
            raise TypeError("attribute should be type string, got {}".format(type(attribute)))
        if not isinstance(incr, int):
            raise TypeError("incr should be type int, got {}".format(type(incr)))

        params = {
            "userId": user_id,
            "userAttributeValuesToIncrement": {
                attribute: incr
            },
            "createDisposition": create_disposition
        }

        self._client.request('POST', 'setUserAttributes', params)
