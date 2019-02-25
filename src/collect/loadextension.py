

import sqlite3

con = sqlite3.connect(":memory:")

# enable extension loading

con.enable_load_extension(True)

#Load the fulltext search extension
# con.execute("select load_extension()")

