# a = 1
# b = 2
# if a < b:
#     print("a is less than b")
#     print("a is difinitely less than b")
# print("Not sure if a is less than b")

# c = 5
# d = 4
# if c < d:
#     print("c is less than b")
# else:
#     print("c is Not less than d")
#     print("I don't think c is less than d")
# print("outside the if block")

# e = 20
# f = 8
# if e < f:
#     print("e is less than f")
# elif e == f:
#     print("e is equal to f")
# elif e > f + 10:
#     print("e is greater than f by more than 10")
# else:
#    print("e is greater than f")

name = "Grevy"
height_m = 1.88
weight_kg = 116.12

bmi = weight_kg / (height_m ** 2)
# the following is how you print two things on the same line using ,end="".
print("BMI: ", end="")
print(bmi)
if bmi < 25:
    print(name, "is not over weight")
else:
    print("Dude you're fat")
