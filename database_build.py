import json
import os

db_structure = {
                    "received_emails":[
                        {
                            "user":os.environ.get('OWNER_EMAIL'),
                            "nickname": "",
                            "messages":[

                            ]
                        }
                    ],
                    "user_list": [os.environ.get('OWNER_EMAIL')]
                }

db = json.loads(str(db_structure).replace("\'","\""))

with open("database.json", 'a') as d:
    final = json.dumps(db, indent=4)
    d.write(final)
