import requests
import ast
import json
url = ("https://matrix.org/_matrix/client/r0/rooms/!VloBXYacCYTNcJpCdx:matrix.org/send/m.room.message?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDI4Y2lkIHVzZXJfaWQgPSBAc2FuZGVlcGtwOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSBCMHI0MWVlT184LUdYOGZPCjAwMmZzaWduYXR1cmUgVpHVfB5VV3Knyr3UwMgxzIZmQG4m_LeYSIfTt1RWEqAK")
msg = raw_input("Enter message to be passed:")
dat = {"msgtype":"m.text", "body":msg}
forward = requests.post(url,data = json.dumps(dat))
d = ast.literal_eval(forward.text)
list = d.keys()
if list[0] == 'event_id':
    print "SUCCESS!!!"
else:
    print "Some error occured"
