from email.message import EmailMessage
from haslos import password
from haslos import sender
import ssl
import smtplib

email_sender = sender
email_password = password
email_receiver = 'example_email@email.com'

subject = "Greetings"
body = """
Greetings from sunny pandora
Hope you are well
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())