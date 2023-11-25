import sqlite3

conn = sqlite3.connect("contacts.sqlite")

# name = input("Please enter a name to search for ")

for row in conn.execute("SELECT * FROM sqlite_master"):
# the name at the end in parathesis has comma with it to make it a tuple. 
# If you do not use a comma you will get a ProgrammingError:
# Incorrect number of bindings supplied. The current statement uses 1, and there are 5 supplied. #noqa
# Also in that line you can use LIKE so that the query does not have to be case sensative. #noqa
    print(row)
conn.close()
