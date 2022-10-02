""" This lesson is to learn how to print data to a text file."""

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# PLANTS_FILENAME  = 'flowers_print.txt'
# This line will print out the text file.
# with open(PLANTS_FILENAME, "w", encoding = 'utf-8') as plants:
#     for plant in data:
#         print(plant, file=plants)

# new_list = []
# with open(PLANTS_FILENAME, encoding = 'utf-8') as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())

# print(new_list)

# PLANTS_FILENAME =  "flowers_write.txt"
# This line of code will write to a text file.
# with open(PLANTS_FILENAME, "w", encoding = 'utf-8') as plants:
#     for plant in data:
#         plants.write(plant)

# print(data)
# string_representation = data.__str__()
# print(type(string_representation))

# If you want complete control over what you gets written, use write.

# Print includes separators, newline, and convert objects to their string representations.

FILENAME = "test.numbers.txt"
with open(FILENAME, "w", encoding='utf-8') as test:
    for i in range(10):
        print(i, file=test) ## The above line of code prints out the range of numbers from 0-9 each on a new line.
with open(FILENAME, 'w', encoding='utf-8') as test:
    for i in range(10):
        # test.write(i) ## This line will give you a TypeError: write () argument must be str, not int. 
        # test.write(str(i)) ## This line will write exactly what you tell it to write. 
        test.write(str(i) + "\n") ## This line will write the range of numbers on a newline using the + "\n". 

### Additional notes on the print and write function.
## The print function will print the string representation of any object that you ask it to print.
# In addition, it will include a separator between multiple arguments- the default is a space, but that can be changed with the sep keyword agrument.

## The write method will only write exactly what you tell it to write. No separators or newline characters are included, unless you explicitly tell it to write them. Also, no conversion is performed. If you tell write to write an integer, that's what it will try to send to the file. If the file is opened in text mode (the default), you'll get an error if you try to write numerical values to it. 

