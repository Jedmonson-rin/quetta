import quickstart
import smtplib
import time
import os

EMAIL_ADDRESS = os.environ.get('QUETTA_EMAIL')
EMAIL_PASSWORD = os.environ.get('QUETTA_PASSWORD')

class Server:
    def __init__(self):
        self.read_messages = []

    def check_messages(self):
        message_list = quickstart.main()
        for message in message_list:
            if message['id'] not in self.read_messages:
                self.send_response(message['from'], message['id'])
                self.read_messages.append(message['id'])
            else:
                self.check_messages()
            

    def send_response(self, email_from, message_id):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            subject = '[Automated-Message] Quetta'
            body = 'Hello I\'m Quetta! My backend services are in development, see you soon!'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADDRESS, email_from, msg)
            print(f'message sent to: {email_from}')

