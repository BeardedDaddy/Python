import random


def get_integer(prompt):
    """_summary_
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.
    
    :param prompt: The string that the user will see, when they're prompted to enter the value.
    :type prompt: int
    :return: The integer that the user enters.
    :type: integer
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))

highest = 1000
answer = random.randint(1, highest)
# print(answer) #TODO: Remove after testing this
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")
    
    if guess == 0:
        break
    if guess == answer:
        print("Damn you finally guessed it.")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else: # guess must be greater than answer
            print("Please guess lower")

# Another way to write this code is the following.
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else: # guess must be greater than answer
       print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly. Please guess again.")
    
#Another way to write this code is the following.
   
    # print("Please guess higher")
    # guess = int(input())
    # if guess == answer:
        # print("Well done, you guessed it")
    # else:
        # print("Sorry, you have not guessed correctly")
# elif guess > answer:
    # print("Please guess lower")
    # guess = int(input())
    # if guess == answer:
        # print("Well done, you guessed it")
    # else: 
        # print("Sorry, you have not guessed correctly")
# else:
    # print("You got it first time")

# In principle elif always comes after if.
#Else always comes after elif
# There are 6 value comparison operators
# Less than <
# Less than or equal to <=
# Greater than >
# Greater than or equal to >=
# Equal to ==
# Not equal to !=
