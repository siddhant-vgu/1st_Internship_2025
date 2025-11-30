import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "siddhantyad12@gmail.com"
APP_PASSWORD = "bqtb nmjy fhjx dthv"
RECEIVER = "karanthenit261104@gmail.com"

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "hellow for python"
msg.set_content("This email was shared by python")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
  server.login(EMAIL,APP_PASSWORD)
  server.send_message(msg)