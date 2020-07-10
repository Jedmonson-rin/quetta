import time
from datetime import datetime

import quickstart

from process_messages import ProcessMessages

class Server:
    def __init__(self):
        self.process_messages = ProcessMessages()
        self.message_list = []
        self.update = True
        self.update_time = "21:30"

    # server entry point
    def runtime(self):
        if self.update_check() is False:
            if self.new_messages():
                if self.process_messages.process(self.message_list):
                    time.sleep(30)
                    self.runtime()
            else:
                print("no messages in the inbox")
                time.sleep(30)
                self.runtime()
        


    # check for new messages
    def new_messages(self):
        print("checking messages")
        message_list = quickstart.main()
        # check to see if message list isnt empty
        if message_list != []:
            self.message_list = message_list
            return True

    def update_check(self):
        if self.update == True and datetime.now().strftime("%H:%M") == self.update_time:
            self.process_messages.update()
        else:
            return False


       
        
            


 
 
        

            

