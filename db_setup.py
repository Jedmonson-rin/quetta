import sqlite3

conn = sqlite3.connect('quetta.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE users (
    email text,
    last_message text
    )""")
conn.commit()
conn.close()