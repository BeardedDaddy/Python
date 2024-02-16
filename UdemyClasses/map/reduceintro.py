"""
The next to lines imports the modules timeit module
and the functools module.
"""
import timeit
import functools


def calc_values(x, y: int):
    """
    This function ask to take to two values and expect
    the an int, then on the next line adds those
    two values.
    """
    return x * y


numbers = [2, 3, 5, 8, 13]

reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)
print(sum(numbers))

RESULT = 1
for x in numbers:
    RESULT *= x
# print(RESULT)

RESULT = calc_values(2, 3)
RESULT = calc_values(RESULT, 5)
RESULT = calc_values(RESULT, 8)
RESULT = calc_values(RESULT, 13)
print(RESULT)
