# age = 50

# name = 'Grevy'

# sentence = 'Hello my name is {} and I am {} years old.'.format(name, age)  # noqa

# print(sentence)
# todayIsCold = False

# print(f'Hello my name is {name} and I am {age} years old.')

# if age >= 18:
#     print('You are of legal age.')
# else:
#     print('You are not old enough.')


def hello(name="Mia", age=13):
    return "Good morning {} you are {} years old.".format (name, age)  # noqa

x = hello()

print(x)
