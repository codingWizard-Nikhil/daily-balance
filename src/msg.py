import os 
from twilio.rest import Client


try:
    import config
    account_sid = config.account_sid
    auth_token = config.auth_token
    twilio_number = config.twilio_number
    user_phone = config.user_phone
except ImportError:
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_number = os.environ.get('TWILIO_NUMBER')
    user_phone = os.environ.get('USER_PHONE')

def create_message(name, balance):
    client = Client(account_sid, auth_token)  
    
    message = client.messages.create(
        body=f"Your {name}'s balance today is ${balance}",
        from_=twilio_number,  
        to=user_phone  
    )
    
    print(f"Message SID: {message.sid}, Status: {message.status}")  
 