from twilio.rest import Client
import twilio
import json
import datetime



# # Find these values at https://twilio.com/user/account
account_sid = 'AC67ad8cc0267ebabd7c9a2b769130087b'
auth_token = '9cd56eed4cc3d6616503150141541c3b'

client = Client(account_sid, auth_token)

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
# client = Client()

# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Your appointment is coming up on July 21 at 3PM',      
#                               to='whatsapp:+923328192943' 
#                           ) 
 
# print(message.sid)
ac = "Walking"
# try:
    # this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+923328192943'

client.messages.create(from_=from_whatsapp_number,
                        body='!!Alert!!\n\nElderly is ' + ac + " at " + str(datetime.datetime.now()),
                        to=to_whatsapp_number)


# except twilio.base.exceptions.TwilioRestException as ex:
#     print(ex)