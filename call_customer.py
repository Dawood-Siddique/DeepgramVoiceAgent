import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(override=True)



class CallCustomer:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    def make_call(self, to_number):
        self.call = self.client.calls.create(
            from_="+12182281566",  # recipient
            to=to_number,
            twiml='<Response><Connect><Stream url="wss://fair-obviously-kite.ngrok-free.app/twilio" /></Connect></Response>'
        )
        return self.call