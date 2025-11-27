from twilio.rest import Client

ACCOUNT_SID = "ACa"
AUTH_TOKEN = "PALCE_YOUR_TOKEN"
TWILIO_NUMBER = ""
RECEIVER_NUMBER = ""
Client = Client(ACCOUNT_SID,AUTH_TOKEN)
message = Client.messages.create(
  body = "hii bro",
  from_ = TWILIO_NUMBER,
  to = RECEIVER_NUMBER)
