

import sqlite3

persons = [
    ("Hugo", "Boss"),
    ("Calvin", "Klein")
]

con = sqlite3.connect(":memory:")

con.execute("create table person(firstname, lastname)")

con.executemany("insert into person(firstname, lastname) VALUES (?,?)", persons)


for row in con.execute("select firstname,lastname from person"):
    print(row)


print("I jst deleted", con.execute("delete from person").rowcount, "rows")


