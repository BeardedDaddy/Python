# def print_backwards(*args, end=' ', **kwargs):
# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)


def print_backwards(*args, **kwargs):
    """ This line of code creates a function called
    print_backwards that has two arguments * args and **kwargs.
    """
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)
    # and print the first word separately  # noqa
    # print(end=end_character)  # which means we don't need this line


def backwards_print(*args, **kwargs):
    """backwards_print is a function
    that has two arguments * args and **kwargs.
    """
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w', encoding='UTF-8') as backwards:
    print_backwards("hello", "planet", "earth",
                    "take", "me", "to", "your", "leader", end='\n')
    print("Another String")


print()
print("hello", "planet", "earth", "take",
      "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take",
                "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)
