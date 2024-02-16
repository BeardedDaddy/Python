def divide_two_numbers(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")


print("Pick two numbers to divide: ")
first_number = divide_two_numbers('First Number ')
second_number = divide_two_numbers('Second Number ')

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))  # noqa
except ZeroDivisionError:
    print("You can't divide by zero")

