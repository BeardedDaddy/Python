""" On the first line we are importing the sys module
"""
import sys


def my_range(n: int):
    """
    This line defines a function named my_range that takes one argument n.
    The : int part is a type hint that indicates n should be an integer.
    Type hints are optional in Python and do not enforce
    the type of the variable, but they can make your code easier to understand.
    """
    print("my_range starts")
    start = 0
    while start < n:
        print(f"my_range is returning {start}")
        yield start
        start += 1


big_range = my_range(5)
_ = input("Line 20, hit enter to continue.")

print(next(big_range))
print(f"big_range is {sys.getsizeof(big_range)} bytes")

# Create a list containing all the values in big_range
big_list = []
_ = input("Line 27, hit enter to continue.")

for val in big_range:
    _ = input("Line 30, hit enter to continue.")
    big_list.append(val)

print(f"big_list is {sys.getsizeof(big_list)} bytes")
print(big_range)
print(big_list)
