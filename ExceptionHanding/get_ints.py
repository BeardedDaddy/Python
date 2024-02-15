import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except: # You should really use except ValueError.
            print("Invalid number entered, please try again")
        # except KeyboardInterrupt:
        #     print("You have exited the program.")
        #     sys.exit(0)
        finally:
            print("The finally clause alway executes")
        
first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number,
                                          first_number / second_number))
except ZeroDivisionError:
    print()
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed succussfully")
           