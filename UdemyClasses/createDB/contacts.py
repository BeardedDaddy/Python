import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")  # noqa
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Grevy', 7542134200, 'grevyjr@gmail.com')")  # noqa
db.execute("INSERT INTO contacts VALUES('MIA', 7542134300, 'mia@gmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.close()
