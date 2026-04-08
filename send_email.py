import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()

mail_password = os.getenv("GOOGLE_APP_PASSWORD")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "jamcoderswe@gmail.com"
    password = mail_password

    reciever = "jamcoderswe@gmail.com"
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)