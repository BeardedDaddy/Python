def print_backwards(*args, **kwargs):
# In the line above we are using the *arg parameter to unpack the tuple or a list. The file parameter to write text data to a file on disk. # noqa
# With the **kwargs we have defined our function to accept **kwargs and whatever appears in there is just passed onto the print function. # noqa
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)
# In this print statement we use the "end=' '"" to continue the end of a string to the same line and not send it to a new line. #noqa
# Adding the "file=file" allows us to print this script to a file. 
# You just add a named peremeter and pass that on to the built-in function, which is what is happening in the next line.   # noqa: E501
with open("backwards.txt", 'w') as backwards:
# The line above first gives the open command to create a text file 'write' to the text file and call the file 'backwards'. # noqa
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards) #noqa
# print_backwards is a modified version of the print function. You then have to add the print parameters file equals the name of the file. #noqa
