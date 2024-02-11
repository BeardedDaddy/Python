"""
This line will import the timeit module.
"""
import timeit

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
        ]
"""
The line below is a variable that has
a list of items.
"""

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("-" * 40)


def spamless_comp():
    """
    This is function called spamless comprehension
    creates an object that loops through the items
    in the menu and displays everything except spam.
    """
    meals = [meal for meal in menu if not_spam(meal)]
    return meals


print("-" * 40)


def not_spam(meal_list: list):
    """
    This line creates a function called
    not_spam that does not have spam in the menu.
    """
    return "spam" not in meal_list


def spamless_filter():
    """spamless_filter is a function that creates a filter
    that only display items in the menu that are not spam.

    Returns
    -------
        it will return variable with a list function that
        will iterate through the menu and display everything
        in the menu but spam.
    """
    spamless_meals = list(filter(not_spam, menu))
    return spamless_meals


if __name__ == '__main__':
    print(spamless_comp())
    print(spamless_filter())
    print(timeit.timeit(spamless_comp, number=1000))
    print(timeit.timeit(spamless_filter, number=1000))
