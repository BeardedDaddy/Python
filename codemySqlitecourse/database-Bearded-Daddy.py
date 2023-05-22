import sqlite3

# Connect to databasd.
conn = sqlite3.connect("customer.db")

# Create a cursor.
c = conn.cursor()

# Create a Table for customer.
# c.execute("""CREATE TABLE customers (
#         first_name TEXT,
#         last _name TEXT,
#         email TEXT
#    ) """)


# print("Command executed successfully")

# many_customers = [
#     ('Mia', 'Marcelin', 'mia@gmail.com'),
#     ('Brittany', 'Johnson', 'brittany@gmail.com'),
#     ('Jennifer', 'Smith', 'jennifer@gmail.com')
# ]
# c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)

c.execute("SELECT * FROM customers")
# print(c.fetchone()) #This one will fetch the first item in the table.
# print(c.fetchmany(3)) #This one will fetch the number you enter in the paratheses.
# print(c.fetchall()) #This one will fetch all of them.

items = c.fetchall()

print("NAME " + "\t\tEMAIL")
print("------" + "\t\t--------")
for item in items:
    print(item[0] + " | " + item[1] + " | " + item[2])
    
# print("Command executed successfully")

# The five DATATYPES below are
# NULL [NO CHAR]
# INTEGER [A NUMBER INT]
# REAL [A NUMBER WITH A DECIMAL]
# TEXT [A TEXT]
# BLOB [A IMAGE]

# Commit commands
conn.commit()

# Close the connection
conn.close()
