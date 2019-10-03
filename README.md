
# python-leanplum

A small python wrapper around Leanplum API (https://docs.leanplum.com/reference#api-introduction)

## Version Compatability
 - 0.5.x - Python 3
 - 0.4.x - Python 2
## Usage

```
from leanplum.client import Client

client = Client(app_id="your_app_id", client_key="your_client_key")

# track events
client.users.track(1234, "custom event")
# advance state
client.users.advance(1234, "Registered")
# set user attributes
client.users.set_user_attributes(1234, {"custom_param": "value"})
# increment attribute
client.users.increment_user_attribute(1234, "Page Views", incr=1)

# delete user
client.admin.delete_user(1234)
```

This wrapper uses the [python-requests](https://github.com/requests/requests) library.  Currently, we don't have a need
to support other network clients, but if we do they will be added as a new ClientImpl(HttpClient). (see leanplum.http_client)

The return object right now is a requests.Response.body, which is a String.
If your request has errors or warnings, some common ones are raised after the response, and you can see some of them
at leanplum.errors

By default, POST requests that handle user behaviors are marked with `createDisposition=CreateNever`.  This may be
modified or made configurable in a later version


TODO:
- requestor better handling of the request (multiple/batch responses?  Right now hard coded to get response[0])
- Response objects for Message, User, State, Event (current return object is a dict)
- More precise Errors to match with Leanplum's wrapped responses
- Add support for croKey and cwoKey, maybe dev/prod mode?