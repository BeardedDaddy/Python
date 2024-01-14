""" On the first line we are importing the sys module
"""
import sys


def my_range(n: int):
    """
    >>> my_range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    print("my_range starts")
    start = 0
    while start < n:
        print(f"my_range is returning {start}")
        yield start
        start += 1


_ = input("line 19")
big_range = my_range(5)
_ = input("line 21")

print(f"big_range is {sys.getsizeof(big_range)} bytes")

# Create a list containing all the values in big_range
big_list = []
_ = input("line 27")

for val in big_range:
    _ = input("line 30 - text inside loop")
    big_list.append(val)

print(f"big_list is {sys.getsizeof(big_list)} bytes")
print(big_range)
print(big_list)
