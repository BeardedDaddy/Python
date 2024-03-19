"""Import time modules to use in the program."""
from calendar import month
import time

# Get the user's name
name = input("Please enter your name? ")
print(" Hello, " + name + " it is nice to meet you.", ("\U0001F603"))
time.sleep(3)

# Baymax introduces himself
print(" My name is Baymax. ")
time.sleep(3)

# Baymax asks the user how their day is going
day = input(" Are you having a wonderful day? (y/n) ")
if day == "y":
    print("That's great to hear " + name + "!", ("\U0001F600"))
elif day == "n":

    # Baymax responds to how is your day.

    print("I'm sorry to hear that " + name + ".", ("\U0001F614"))
else:
    print(" Please enter an y for yes or n for no " + name + "?")

# Baymax asks the user how old they are

age = int(input("How old are you? "))
time.sleep(3)

if age <= 18:
    print("You look young for your age.")


def get_zodiac_Sign(month, day):
    """Gets the zodiac Sign for a given date of birth.

  Args:
    month: The month of birth, as a string.
    day: The day of birth, as an integer.

  Returns:
    The zodiac Sign, as a string.
    """


Signs = {
    "december": {
        "sagittarius": (22, 31),
        "capricorn": (1, 21)
    },
    "january": {
        "capricorn": (1, 19),
        "aquarius": (20, 31)
    },
    "february": {
        "aquarius": (1, 18),
        "pisces": (19, 29)
    },
    "march": {
        "pisces": (1, 20),
        "aries": (21, 31)
    },
    "april": {
        "aries": (1, 19),
        "taurus": (20, 30)
    },
    "may": {
        "taurus": (1, 20),
        "gemini": (21, 31)
    },
    "june": {
        "gemini": (1, 20),
        "cancer": (21, 30)
    },
    "july": {
        "cancer": (1, 22),
        "leo": (23, 31)
    },
    "august": {
        "leo": (1, 22),
        "virgo": (23, 31)
    },
    "september": {
        "virgo": (1, 22),
        "libra": (23, 30)
    },
    "october": {
        "libra": (1, 22),
        "scorpio": (23, 31)
    },
    "november": {
        "scorpio": (1, 21),
        "sagittarius": (22, 30)
    }
}

Sign = None
for month_name, month_data in Signs.items():
    if month_name == month:
        for Sign_name, Sign_dates in month_data.items():
            if day >= Sign_dates[0] and day <= Sign_dates[1]:
                Sign = Sign_name
                break
        return Sign


def main():
    """Gets the zodiac Sign for the user's date of birth."""
    month = input("Enter your birth month: ")
    day = int(input("Enter your birth day: "))  
    Sign = get_zodiac_Sign(month, day)  
    print(f"Your zodiac Sign is {Sign}.")


if __name__ == "__main__":
  main()

# answer = input("You are very beautiful")
# if answer == " Thank you":
#     print("You're welcome beautiful.")
# else:
#     print("Ahhh you shy?", print("\U0001F97A"))
#     time.sleep(3)
#     print("I understand.")
#     time.sleep(3)
