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
