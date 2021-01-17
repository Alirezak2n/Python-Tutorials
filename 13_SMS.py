from twilio.rest import Client
from credential_13 import account_sid,auth_token,my_cell,my_twilio

client = Client(account_sid, auth_token)

my_msg = ''.join('successful Alireza\n' for i in range(10))

message = client.messages.create(to=my_cell, from_ = my_twilio,
                                 body = my_msg)



