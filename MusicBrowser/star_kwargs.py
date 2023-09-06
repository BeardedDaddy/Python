# def print_backwards(*args, end=' ', **kwargs):
# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     kwargs.pop("end", None)
#     # In the line above we are using the *arg parameter to unpack the tuple or a list. The file parameter to write text data to a file on disk. # noqa
#     # With the **kwargs we have defined our function to accept **kwargs and whatever appears in there is just passed onto the print function. # noqa
#     for word in args[::-1]:
#         print(word[::-1], end=" ", **kwargs)

#     print(kwargs)
#     kwargs.pop("end", None)
#     # In the line above we are using the *arg parameter to unpack the tuple or a list. The file parameter to write text data to a file on disk. # noqa
#     # With the **kwargs we have defined our function to accept **kwargs and whatever appears in there is just passed onto the print function. # noqa
#     for word in args[::-1]:
#         print(word[::-1], end=" ", **kwargs)


def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)   # and print the first word separately #noqa
    # print(end=end_character)  # which means we don't need this line


# In this print statement we use the "end=' '"" to continue the end of a string to the same line and not send it to a new line. #noqa
# Adding the "file=file" allows us to print this script to a file.
# You just add a named peremeter and pass that on to the built-in function, which is what is happening in the next line.   # noqa: E501
def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)
    
with open("backwards.txt", "w") as backwards:
    # The line above first gives the open command to create a text file 'write' to the text file and call the file 'backwards'. # noqa
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end="n")  # noqa
    print("Another String")
# print_backwards is a modified version of the print function. You then have to add the print parameters file equals the name of the file. #noqa

print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')  # noqa
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end="n", sep='\n**\n')  # noqa
print("=" * 10)
