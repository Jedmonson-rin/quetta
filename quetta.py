import time

import quickstart

from process_messages import ProcessMessages

class Server:
    def __init__(self):
        self.process_messages = ProcessMessages()
        self.message_list = []

    # server entry point
    def runtime(self):
        self.new_messages()
        if self.message_list != []:
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
       
        
            


 
 
        

            

