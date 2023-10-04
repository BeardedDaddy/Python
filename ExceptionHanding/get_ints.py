import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
# if a valid number is entered in line 7 the code is just going to continue
# and the number will just be returned. #noqa
            return number
        except EOFError:  # You should really use except ValueError.
            # If an invalid input is entered a ValueError except will be
            # raised. #noqa
            # except KeyboardInterrupt:
            # print("You have exited the program.")
            # sys.exit is used to exit the program.
            sys.exit(0)
        except Exception:
            print("Invalid number entered, please try again")
        # a finally clause always comes after the except clause.The finally 
        # block can be used to closing your cursor or connectioning or closing any open files.  # noqa
        # The finally is always excuted even if there is an exception even if
        # the program is terminated.
        finally:
            print("The finally clause alway executes")


# the script below ask the user for two numbers.
first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")
# the code below is a try block that will catch a ZeroDivisionError if you try to divide by zero.  # noqa
try:
    print("{} divided by {} is {}".format(first_number, second_number,  # On
                                          # this line we are using replacement fields.  # noqa
                                          # This .format has three parameters inside the parentheis.  # noqa
                                          first_number / second_number))
except ZeroDivisionError:
    print()
    print("You can't divide by zero")
    sys.exit(2)
    # the else clause in a while loop will execute if the loop terminate
    # normally. If there is no break or return statement. When you use a try
    # block in your code the else is always added at the end of except clauses
    # but before any finally clause.
else:
    print("Division performed succussfully")
