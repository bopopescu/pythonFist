
import sqlite3

con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row


cur = con.cursor()
cur.execute("select 'John' as name, 42 as age")
for row in cur:
    print(row[0] == row["name"])
    print(row["name"] == row["nAmE"])



