import sqlite3

# define a connection and cursor

conn = sqlite3.connect('store_transactions.db')

cursor = conn.cursor()

# create a store table

command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

# create a purchase table

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

# add three rows to our stores table

cursor.execute("INSERT INTO store VALUES (21, 'Minneapolis, MN')")
cursor.execute("INSERT INTO store VALUES (95, 'Chicago, IL')")
cursor.execute("INSERT INTO store VALUES (64, 'Iowa City, IA')")

# add to our purchases table

cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")

# get results

cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)
