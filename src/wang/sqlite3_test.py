
import sqlite3


conn = sqlite3.connect('first.db')
c = conn.cursor()
c.execute('''create table user_tb(
    _id integer primary key autoincrement,
    name text,
    pass text, 
    gender text)''')


c.close()
conn.close()


