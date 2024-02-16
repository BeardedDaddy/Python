"""
The code below imports the timeit module.
"""
import timeit

"""The code below is a variable that has a string"""
TEXT = "what have the romans ever done for us"


def comp_caps():
    """
    The code snippet below is a function
    that changes the text character to uppercase.
    """
    capitals = [char.upper() for char in TEXT]
    return capitals


# use map
def map_caps():
    """
    The code snippet below is a function
    that changes the text string to uppercase.
    """
    map_capitals = list(map(str.upper, TEXT))
    return map_capitals


def comp_words():
    """
    The code snippet below is a function
    that changes the text words to uppercase.
    """
    words = [word.upper() for word in TEXT.split(' ')]
    return words


# use map
def map_words():
    """
    The code snippet below is a function
    that changes the list of text words to uppercase.
    """
    map_w = list(map(str.upper, TEXT.split(' ')))
    return map_w


# The code below is how you call the print the functions above.

if __name__ == '__main__':
    print(comp_caps())
    print(map_caps())
    print(comp_words())
    print(map_words())
    # print(timeit.timeit("comp_caps()", setup="from map_intro import comp_caps", number=10000))  # noqa
    # The above line of code runs the timeit function for all the functions in this module.  # noqa
    print(timeit.timeit(comp_caps, number=10000))
    print(timeit.timeit(map_caps, number=10000))
    print(timeit.timeit(comp_words, number=10000))
    print(timeit.timeit(map_words, number=10000))
    # The above lines of code runs the timeit function for each function seperately.  # noqa
    # In the print statements when passing the function we are not using
    # parentheses. We're passing a reference to the function, not a function
    # call. If you were to try to call the function, you'll get an error.
