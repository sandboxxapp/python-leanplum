from leanplum.client import Client

APP_ID = "your-app-id"
CLIENT_KEY = "your-client-key"

client = Client(APP_ID, CLIENT_KEY)

client.users.track(133700, event="Joined Faction", params={"Faction Name": "Rebels"})
client.users.advance(133700, state="Member", params={"Membership": "Rebel Scum"})
client.users.set_user_attributes(133700, {"email": "wookie@milleniumfalcon.com"})
