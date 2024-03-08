import time
import emoji

# Get the user's name
name = input("Please enter your name? ")
# print(" Hello, " + name + " it is nice to meet you.", emoji.emojize(":grinning_face_with_big_eyes:"))
print(" Hello, " + name + " it is nice to meet you.", ("\U0001F603"))
time.sleep(3)
print(" My name is Baymax. ")
time.sleep(3)
day = input(" Are you having a wonderful day? (y/n) ")
if day == "y":
    print("That's great to hear " + name + "!", ("\U0001F600"))
elif day == "n":
    print("I'm sorry to hear that " + name + "", ("\U0001F614"))
else:
    print(" Please enter an y for yes or n for no " + name + "?")
