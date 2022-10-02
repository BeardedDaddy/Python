flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]
# The following print statement will print the list of 'Flowers' in square brackets.
# print(flowers)
# print()

# The following print statement will loop through the list printing the each flower on an new line.
# for flower in flowers:
#     print(flower)

# The following print statement will print each flower on one line using the pipe character or bar to separator each named flower. Joining the them all using the .join (a string method). We are using a string called separator to indicate what we are doing. Dot 'join' has to to connected to a string to work. Note the string method .join can only join strings. If you enter a int into a list your code will crash. Example Iris | Lavender | 76 . This will not work. 
print()
separator = " | "
output = separator.join(flowers)
print(output)