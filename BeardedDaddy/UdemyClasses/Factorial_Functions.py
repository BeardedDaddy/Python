# The factorial of a number is the product of all the values from 1 to the number, inclusive.
# Thus 4 factorial, which is written as 4!, is calculated as
# 1*2*3*4=24
# 5! is
# 1*2*3*4*5=120
# The convention is that 0!=1 (not zero, as you might expect)

# Write a function called factorial, that will return the factorial of the number passed as its argument.
# You must include a Docstring, and function annotations, in your function.

# Use a for loop to call your factorial function, to print out the first 36 factorials (0 to 35). Your results should be:
# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120 .....


def fact(n):

    f = 1

    for i in range(1,n+1):
        f = f*i

    return f
x = 5

result = fact(x)


print(result)