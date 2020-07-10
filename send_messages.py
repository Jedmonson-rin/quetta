import os
import smtplib
import json

class SendMessages:
    def __init__(self):
        self.email_address = os.environ.get('QUETTA_EMAIL')
        self.email_password = os.environ.get('QUETTA_PASSWORD')
        self.owner_email = os.environ.get('OWNER_EMAIL')
        self.responses = self.load_responses()

    # load responses.json
    def load_responses(self):
        with open('responses.json', 'r') as j:
            responses = json.load(j)
        return responses


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
        email_subject = self.responses['deprecated']['subject']
        email_body = self.responses['deprecated']['body']
        email_msg = f'Subject: {email_subject}\n\n{email_body}'
        self.login(email, email_msg)
        print(f'deprecated message sent to: {email}')

    # Send New User Response
    def new_user_resp(self, email):
        print("sending NU resp.")
        email_subject = self.responses['introduction']['subject']
        email_body = self.responses['introduction']['body']
        email_msg = f'Subject: {email_subject}\n\n{email_body}'
        self.login(email, email_msg)
        print(f'introduction message sent to: {email}')

    def shutdown_confirmation(self, email):
        email_subject = self.responses['shutdown']['subject']
        email_body = self.responses['shutdown']['body']
        email_msg = f'Subject: {email_subject}\n\n{email_body}'
        self.login(email, email_msg)
        print(f'message sent to: {email}')
        return True
    
    def update_confirmation(self, email):
        email_subject = self.responses['update']['subject']
        email_body = self.responses['update']['body']
        email_msg = f'Subject: {email_subject}\n\n{email_body}'
        self.login(email, email_msg)
        print(f'message sent to: {email}')
        return True