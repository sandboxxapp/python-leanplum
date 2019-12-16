from leanplum.actions.abstract import BaseResource
from leanplum.actions import disposition

__all__ = ['Users']


class Users(BaseResource):

    def advance(self, user_id, state, info=None, params=None, create_disposition=disposition.CREATE_NEVER):
        """
        https://docs.leanplum.com/reference#post_api-action-advance

        :param user_id: REQUIRED The current user ID
        :param str state: REQUIRED The name of the state
        :param str info: Any info attached to the state.
        :param dict params: A flat object of parameters as key-value pairs.
        :param str create_disposition: The policy that determines whether users are created by the API. Default: CreateNever
        :return: The response from Leanplum api
        """

        if not user_id:
            raise ValueError("user_id is a required field")
        if not state:
            raise ValueError("state is a required field")
        if not isinstance(state, str):
            raise TypeError("state should be type string, got {}".format(type(state)))

        if params and not isinstance(params, dict):
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
        if not isinstance(event, str):
            raise TypeError("event should be type string, got {}".format(type(event)))

        if params and not isinstance(params, dict):
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

    def set_user_attributes(self, user_id=None, new_user_id=None, attributes=None, attributes_to_add=None, attributes_to_remove=None,
                            create_disposition=disposition.CREATE_NEVER, **kwargs):
        """
        https://docs.leanplum.com/reference#post_api-action-setuserattributes

        :param user_id: REQUIRED The current user ID
        :param new_user_id: The new user ID to update this user with
        :param dict attributes: A map of user attributes as key-value pairs.
        :param dict attributes_to_remove: A map of values to add to existing user attribute sets.
        :param dict attributes_to_add: A map of values to remove from existing user attribute sets.
        :param str create_disposition: The policy that determines whether users are created by the API. Default: CreateNever
        :param kwargs: Any extra params to put on the request.  Note: use camelCase on these params
        :return: The response from Leanplum api
        """

        if not user_id:
            raise ValueError("user_id is a required field")

        if attributes and not isinstance(attributes, dict):
            raise ValueError("SetUserAttributes attributes param must be of type dict")

        params = {
            "userId": user_id,
            "newUserId": new_user_id,
            "userAttributes": attributes,
            "userAttributeValuesToAdd": attributes_to_add,
            "userAttributeValuesToRemove": attributes_to_remove,
            "createDisposition": create_disposition
        }

        params.update(kwargs)

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
        if not isinstance(attribute, str):
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
