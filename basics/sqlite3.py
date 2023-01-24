# import db
import sqlite3

# connect db with file
connect = sqlite3.connect('client.db')

# connect.execute("DROP TABLE IF EXIST")

# create DB
# connect.execute('''CREATE TABLE CLIENT (
#     ID INT PRIMARY KEY NOT NULL, 
#     NAME TEXT NOT NULL, 
#     AGE INT NOT NULL
# );''')

# Insert data in the DB
connect.execute("INSERT INTO CLIENT (ID,NAME,AGE) VALUES (1, 'Anna', 28)")
connect.execute("INSERT INTO CLIENT (ID,NAME,AGE) VALUES (2, 'Joe', 46)")

# Get data from DB
data = connect.execute('''SELECT * FROM CLIENT''')

# Print data
for row in data:
    print(row)

connect.close()