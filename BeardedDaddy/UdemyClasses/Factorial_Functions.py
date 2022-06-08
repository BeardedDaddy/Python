
# The factorial of a number is the product of all the values from 1 to the number, inclusive.
# Thus 4 factorial, which is written as 4!, is calculated as
# 1*2*3*4=24
# 5! is
# 1*2*3*4*5=120
# The convention is that 0!=1 (not zero, as you might expect)

#Write a function called factorial, that will return the factorial of the number passed as its argument.
# You must include a Docstring, and function annotations, in your function.

#Use a for loop to call your factorial function, to print out the first 36 factorials (0 to 35). Your results should be:
# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120 .....


def my_factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    if n <= 1:
        return 1

    result = 2
    for n in range(3, n + 1):
        result *= n

    return result


for i in range(36):
    print(i, my_factorial(i))
