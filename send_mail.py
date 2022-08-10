import smtplib
import ssl
from email.message import EmailMessage

import secrets

def sendMail(receiver_email, username, usage, table=""):
    sender_email = secrets.email 
    password = secrets.password

    subject = "Daily update from netman"
    body = "Hi " + username + ",\n"
    usage = str(usage)

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    
    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
            <p>Your IUT internet usage so far is {usage}</p>
            {table}
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    print("Sending email to " + username, end=": ")


    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("successful!")

