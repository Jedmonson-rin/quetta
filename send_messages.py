import os
import smtplib

class SendMessages:
    def __init__(self):
        self.email_address = os.environ.get('QUETTA_EMAIL')
        self.email_password = os.environ.get('QUETTA_PASSWORD')
        self.owner_email = os.environ.get('OWNER_EMAIL')

    # Initiate SMTP Connection
    def login(self, email, email_msg):
        print("initiating SMTP connection.")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.email_address, self.email_password)
            smtp.sendmail(self.owner_email, email, email_msg)

   # Send Standard Response
    def standard_resp(self, email):
        print("sending standard response.")
        with open("responses/deprecated.txt", 'r') as d:
            deprecated = d.read().split('\n')
        email_subject = deprecated[0]
        email_body = deprecated[1]
        email_msg = f'Subject: {email_subject}\n\n{email_body}'
        self.login(email, email_msg)
        print(f'deprecated message sent to: {email}')

    # Send New User Response
    def new_user_resp(self, email):
        print("sending NU resp.")
        with open("responses/introduction.txt", 'r') as d:
            introduction = d.read().split('\n')
        email_subject = introduction[0]
        email_body = introduction[1]
        email_msg = f'Subject: {email_subject}\n\n{email_body}'
        self.login(email, email_msg)
        print(f'introduction message sent to: {email}')

    def shutdown_confirmation(self, message):
        if "shutdown" in message:
            print("sending shutdown confirmation")
            email_subject = '[Automated-Message] Quetta-Shutdown'
            email_body = 'Shutting down boss.'
            email_msg = f'Subject: {email_subject}\n\n{email_body}'
            self.login(self.OWNER_EMAIL, email_msg)
            print(f'message sent to: {self.OWNER_EMAIL}')
            return True