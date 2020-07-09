from db_manage import DbManage
from send_messages import SendMessages


class ProcessMessages:
        def __init__ (self):
            self.database = DbManage()
            self.send_message = SendMessages()
            
        def process(self, message_list):
            for message in message_list:
                if self.check_user(message['from']):
                    if self.new_message(message['from'], message['id']):
                        if self.shutdown_check(message['from'], message['snippit'])

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

        def shutdown_check(self, email, message_id):
