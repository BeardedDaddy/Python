name = input("Please enter name: ")
age = int(input(f"How old are you, {name} ? "))
# print("Oh ", age)

# if age >= 18:
#     print("You are old enough to vote.")
# else:
#     print(f"Please come back in {18 - age} years {name}.")

message = f"You are old enough to vote {name}." if age >= 18 \
    else f"Please come back in {18 - age} years {name}."
print(message)
