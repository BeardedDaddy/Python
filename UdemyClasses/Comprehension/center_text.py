"""
This function takes any number of arguments, converts them to strings,
and centers them in an 80-character wide terinal.
Each argument is separated by a space.

Args:
    *args: Any number of arguments, which can be of any type.
    Each argument will be converted to a string.
    
Returns:
    None. This function prints the centered text but does not return it.
"""


def centre_text(*args):
    """This line creates a function called
    centre_text with an *args argument."""
    # text = ""
    # for arg in args:
    #     text += str(arg) + " "
    text = "-".join([str(arg) for arg in args])  # This is a list comprehension.  # noqa
    # text = "-".join(str(arg) for arg in args) # This is a generator expression.  # noqa
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")
