import smtplib
import ssl
import config

port = 465
sender = config.FromEmailAdd
password = config.Password


message = """\
Subject:Automated Python Email

This is an automated email sent from python!

Regards,
Yousaf Irshad
"""

context = ssl.create_default_context()

print("Starting to send emails\n")

for x in range(len(config.ToEmailAdd)):
    receive = config.ToEmailAdd[x]
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receive, message)
    print("Email "+str(x+1)+" sent!\n")

print("All Emails Sent!")
