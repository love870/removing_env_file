import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC8843382db00b8fb49204a2da7c2fbdef"
auth_token = "7534ad0a41ffdbfdfa1fe87b1fcb3a7c"
client = Client(account_sid, auth_token)
try:
    message = client.messages.create(
                                body='Hi Love Aggarwal',
                                from_='+15802278916',
                                to='+918708919421'
                            )
except Exception as e: 
    print(str(e))
