
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# # Create table
#
# c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#
# #Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'IBM', 1000, 45.00)")
# c.execute("INSERT INTO stocks VALUES ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00)")
# c.execute("INSERT INTO stocks VALUES ('2006-04-06', 'BUY', 'IBM', 500, 53.00)")
# # Save commit the changes
#
# conn.commit()
# conn.close()

# symbol = 'RHAT'

# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# print(c.fetchone())

# purchase = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#             ('2006-04-06', 'SELL', 'IBM', 500, 53.00)]
#
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchase)
# conn.commit()
# conn.close()


for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
























