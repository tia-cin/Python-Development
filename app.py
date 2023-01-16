import sqlite3

connect = sqlite3.connect('client.db')

# connect.execute("DROP TABLE IF EXIST")
# connect.execute('''CREATE TABLE CLIENT (
#     ID INT PRIMARY KEY NOT NULL, 
#     NAME TEXT NOT NULL, 
#     AGE INT NOT NULL
# );''')

connect.execute("INSERT INTO CLIENT (ID,NAME,AGE) VALUES (1, 'Anna', 28)")

connect.close()