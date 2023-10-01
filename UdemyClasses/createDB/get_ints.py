def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")


first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {:.2f}".format(first_number, second_number, first_number / second_number))   # noqa
except ZeroDivisionError:
    print("You can't divide by zero")
