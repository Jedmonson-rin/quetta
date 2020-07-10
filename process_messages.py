import os
from datetime import datetime

from db_manage import DbManage
from send_messages import SendMessages



class ProcessMessages:
        def __init__ (self):
            self.database = DbManage()
            self.send_message = SendMessages()
            self.owner_email = os.environ.get('OWNER_EMAIL')

        def process(self, message_list):
            for message in message_list:
                if self.check_user(message['from']):
                    if self.new_message(message['from'], message['id']):
                        if message['from'] == self.owner_email:
                            self.management(message['message'])
                        self.standard_message(message['from'])
                    return True
                else:
                    print("this user does not exist   ---adding user")
                    if self.add_user(message['from'], message['id']):
                        print("user added")
                        return True
                    
        def check_user(self, message):
            if self.database.check_user(message):
                return True

        # need to add whitelisting functionality
        def add_user(self, email, message_id):
            if self.database.add_user(email, message_id):
                print("sending introduction message")
                self.send_message.new_user_resp(email)
            return True

        def standard_message(self, email):
            self.send_message.standard_resp(email)

        def new_message(self, email, message_id):
            print("checking for new messages")
            if self.database.new_message_id(email, message_id):
                return True

        def shutdown(self, email, body):
                print("sending shutdown confirmation")
                self.send_message.shutdown_confirmation(self.owner_email)
                print("closing db connection")
                self.database.close_connection()
        
        def update(self):
            print("updating, sending shutdown confirmation")
            self.send_message.update_confirmation(self.owner_email)
            print("closing db connection")
            self.database.close_connection()

        def management(self, body):
            if "shutdown" in body:
                self.shutdown()
                exit()
            if "update" in body:
                self.update()
                os.system("python3 update.py")
                exit()
            else:
                pass


