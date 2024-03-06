dognames = ["Fido", "Sean", "Sally", "Mark", "Sean"]

# print(dognames)
dognames.insert(0, "Pepe")

del(dognames[3])  # del deletes an item from the list. # From dognames delete index 3 which = Mark.  # noqa
# print(dognames)

print(dognames[2])  # prints Sally

dognames[1] = "Jane"  # replaces Sean with Jane

print(len(dognames))  # prints 5

print(dognames)  # prints ['Pepe', 'Fido', 'Sean', 'Sally', 'Sean']
