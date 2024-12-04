import sqlite3

conn = sqlite3.connect('database.db')
print("database.db is connected")

conn.execute('CREATE TABLE info (name TEXT,description TEXT)')
print("Table created successfully!")

#Drop commands
#conn.execute('DROP TABLE info')
#print("Table info dropped successfully")

conn.close() #close conection
print("Session Closed")