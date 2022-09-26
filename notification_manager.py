from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, SID, SKEY, ANUM):
        self.SID = SID
        self.SKEY = SKEY
        self.ANUM = ANUM

    def send_sms(self, message, phone):
        client = Client(self.SID, self.SKEY)
        message = client.messages.create(
            body=message,
            from_=self.ANUM,
            to=phone
        )
        return message
