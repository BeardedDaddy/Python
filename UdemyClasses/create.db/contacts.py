import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")# noqa
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Grevy, 9542179824, grevy@gmail.com')")  # noqa: E501
db.execute("INSERT INTO contacts VALUES('Mia', 37373,'mia@gmail.com' )") # noqa

db.close()
