import config
from twilio.rest import Client

def create_message(name, balance):

    client = Client(config.account_sid, config.auth_token)

    message = client.messages.create(
        body = f"Your {name}'s balance today is ${balance}",
        from_ = config.twilio_number,
        to = config.user_phone
    )


    print(message.sid, message.status)
 