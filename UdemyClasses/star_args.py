 """This function creates a class that builds a tuple with the argument * args."""  # noqa
 def build_tuple(*args):
   # return args

 message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")  # noqa: E501
 print(type(message_tuple))
 print(message_tuple)

 number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
 print(type(number_tuple))
 print(number_tuple)

#def average(args):
#    """This function is class called average with an argument of * args."""
#    # The * unpacks the args argument as tuple (average(1, 2, 3, 4))
#    # Without the * you get a TypeError indicating that 1 positional argument but 4 were given.  # noqa
#    # To print it without the *args you would have to put a second set of parenthesis around the ((1, 2, 3, 4))  # noqa
#    print(type(args))
#    print(f"args is {args}:")
#    print("*args is:", *args)
#    mean = 0
#    for arg in args:
#        mean += arg
#    return mean / len(args)
#
#
#print(average((1, 2, 3, 4)))
