# """This function creates a class that builds
# a tuple with the argument * args."""  # noqa
# def build_tuple(*args):
#    return args
# message_tuple = build_tuple("hello", "planet", "earth",
# "take", "me", "to", "your", "leader")  # noqa: E501
# print(type(message_tuple))
# print(message_tuple)
# number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
# print(type(number_tuple))
# print(number_tuple)

# def average(args):
#    """This function is class called average with an argument of * args."""
#    # The * unpacks the args argument as tuple (average(1, 2, 3, 4))
#    # Without the * you get a TypeError indicating that 1
# positional argument but 4 were given.  # noqa
#    # To print it without the *args you would have to put a
# second set of parenthesis around the ((1, 2, 3, 4))  # noqa
#    print(type(args))
#    print(f"args is {args}:")
#    print("*args is:", *args)
#    mean = 0
#    for arg in args:
#        mean += arg
#    return mean / len(args)
#
#
# print(average((1, 2, 3, 4)))


#def print_backwards(*args, end=' ', **kwargs):
#def print_backwards(*args, **kwargs):
#    """This function creates a class called print_backwards 
#    with *args and **kwargs as the argument."""  # noqa+
#    print(kwargs)
#    kwargs.pop('end', None)
#    for word in args[::-1]:
#        print(word[::-1], end=' ', **kwargs)


def print_backwards(*args, **kwargs):
    """This function creates a class called print_backwards 
    with *args and **kwargs as the argument."""  # noqa+
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)   # and print the first word seperately.  # noqa
#    print(end=end_character)   # which means we don't need this line


def backwards_print(*args, **kwargs):
    """This function creates a class called backwards_print 
    with *args and **kwargs as the argument."""  # noqa+
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

with open("backwards.txt", 'w', encoding='utf-8') as backwards:
    print_backwards(
        "Hello planet earth take me to your leader", end='\n')
    print("Another String")


print()
print_backwards(
    "Hello", "planet", "earth", "take", "me", "to", "your", "leader", end=' ', sep='\n**\n')
print(
    "Hello", "planet", "earth", "take", "me", "to", "your", "leader", end=' ', sep='\n**\n')
print("=" * 10)
