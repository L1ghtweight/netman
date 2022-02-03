import smtplib
import ssl
from getpass import getpass
import secrets

def sendMail(r_email, message):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = secrets.email

    password = secrets.password

    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)

        server.ehlo()

        server.login(sender_email, password)
        server.sendmail(sender_email, r_email, message)
