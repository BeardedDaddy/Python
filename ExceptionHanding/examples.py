def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(900))
except (RecursionError, ZeroDivisionError, OverflowError):
    print("Whoa whoa whoa, you can't do that.")

print("Program terminating")
