# Write a fuction to calculate the sum of all numbers passed as its arguments.
def sum_numbers(*values: float) -> float:
    """Call the function sum_numbers"""
    result = 0
    for number in values:
        result += number
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(7, 4, 24))
print(sum_numbers(14.7, 2.976, 84.7))
print(sum_numbers(3.9, 4.2, 5.0))
# The numbers in the square bracket are the parameters that are going to be passed as the argument.
# It should define a single variable argument (a star argument) that will get the values to sum.

# This function must contain a Docstring.

# The parameters must be annotated.

# The return value must be annotated.
