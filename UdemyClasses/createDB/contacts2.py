import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter a phone number ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)  # noqa
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"  # noqa

# print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
# this is the same as db.commit() # calling dot commit on the wrong connection could cause bugs. # noqa
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(phone)
    print(name)
    print(email)
    print("-" * 20)

# cursor.close()
db.close()
