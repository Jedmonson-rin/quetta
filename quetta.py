import quickstart
import smtplib
import time
import os
import json

class Server:
    def __init__(self):
        self.database = ''
        self.EMAIL_ADDRESS = os.environ.get('QUETTA_EMAIL')
        self.EMAIL_PASSWORD = os.environ.get('QUETTA_PASSWORD')
        self.OWNER_EMAIL = os.environ.get('OWNER_EMAIL')


    def load_db(self):
        with open('database.json', 'r') as db:
            self.database = json.load(db)

    def save_db(self):
        with open("database.json", 'w') as db:
            json.dump(self.database, db, indent = 6) 

    # server entry point
    def runtime(self):
        self.load_db()
        self.check_messages()


    # check for new messages
    def check_messages(self):
        print("checking messages")
        message_list = quickstart.main()
        # check to see if message list isnt empty
        if message_list != []:
            for message in message_list:
                # if the message isnt in the database as a processed message
                if self.check_message(message['id']) is not True:
                    # if the user has accessed the bot before
                    if self.check_user(message['from'], message['id']):
                        if message['from'] == self.OWNER_EMAIL:
                            if self.check_shutdown(message['message']):
                                self.save_db()
                                print("shutting down")
                                exit()
                        self.send_resp(message['from'], message['id'])
                        for entry in self.database['received_emails']:
                            if entry['user'] == message['from']:
                                entry['messages'].append(message['id'])
                        time.sleep(30)
                        self.check_messages()
                        print(self.database)
                    # if the user has not accessed the bot before
                    else:
                        self.send_NU_resp(message['from'], message['id'])
                        time.sleep(30)
                        self.check_messages()
                        print(self.database)
                # keep checking messages
                else:
                    time.sleep(30)
                    self.check_messages()
                    print(self.database)
        else:
            time.sleep(30)
            self.check_messages()

    # check to see if this user has used the bot
    def check_user(self, user, message_id):
        print("checking to see if the user has been here before.")
        if user in self.database['user_list']:
            return True
        else:
            self.database['user_list'].append(user)
            self.database['received_emails'].append({
                        "user": user,
                        "nickname": "unknown",
                        "messages":[message_id]
                    })

    def check_message(self, message_id):
        print("checking message id to see if it has been processed.")
        for entry in self.database['received_emails']:
            if message_id in entry['messages']:
                return True

    # Send Standard Response
    def send_resp(self, user, message_id):
        print("sending standard response.")
        email_subject = '[Quetta-Automated] Deprecated'
        email_body = 'Hello! My backend services are in development, see you soon!\n\n\nQuetta,'
        email_msg = f'Subject: {email_subject}\n\n{email_body}'
        self.login(user, email_msg)
        print(f'message sent to: {user}')

    # Send New User Response
    def send_NU_resp(self, user, message_id):
        print("sending NU resp.")
        email_subject = '[Quetta-Automated] Introduction'
        email_body = 'Hello it\'s nice to meet you! Please send me another message with your name so I know who you are. \n\nexample: name - <your_name_here> \n\n\nQuetta,'
        email_msg = f'Subject: {email_subject}\n\n{email_body}'
        self.login(user, email_msg)
        print(f'introduction message sent to: {user}')

    # Initiate SMTP Connection
    def login(self, user, email_msg):
        print("initiating SMTP connection.")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
            smtp.sendmail(self.EMAIL_ADDRESS, user, email_msg)


    def check_shutdown(self, message):
        if "shutdown" in message:
            print("sending shutdown confirmation")
            email_subject = '[Automated-Message] Quetta-Shutdown'
            email_body = 'Shutting down boss.'
            email_msg = f'Subject: {email_subject}\n\n{email_body}'
            self.login(self.OWNER_EMAIL, email_msg)
            print(f'message sent to: {self.OWNER_EMAIL}')
            return True
        

            

