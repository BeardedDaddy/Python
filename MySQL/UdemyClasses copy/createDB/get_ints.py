import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(0)
        except KeyboardInterrupt:
            print()
            print("Keyboard interrupt detected")
            sys.exit()
        finally:
            print("Good choice, that is a good number.")


first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {:.2f}".format(first_number, second_number, first_number / second_number))   # noqa
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")
