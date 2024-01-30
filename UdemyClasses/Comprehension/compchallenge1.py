# Create a new Python file - I've called this one "FIZZBUZZ.py".
#
# Use the conditional expression from the previous video to produce
# a list comprehension that returns the FIZZBUZZ results.
#
# If a number's divisible by 3, the value should be "fizz".
# If it's divisible by 5, the value should be "buzz".
# If it's divisible by both 3 and 5, the value should be "fizz buzz"
# Finally, if none of those conditions apply, the value will be the number itself.  # noqa
#
# The code from the end of the last video appears below, so you can check the result.  # noqa

# for x in range(1, 31):
#     FIZZBUZZ = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
#     print(FIZZBUZZ)

fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
            for x in range(1, 31)]
print(fizzbuzz)

for buzz in fizzbuzz:
    print(buzz.center(12, '*'))  # This will print the output using 12 characters in the centered by asterisks.  # noqa
