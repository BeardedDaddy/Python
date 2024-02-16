"""
This line of code initializes a list named 'burgers'
with three string elements: "beef", "chicken", and "spicy bean".
These represent different types of burgers.
"""
burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

for meals in [(burger, toppings) for burger in burgers for topping in toppings]:
    print(meals)
# The above code is a nested list comprehension.
print()

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))
# The above code is a nested for loop.

for nested_meals in [[(burger, toppings) for burger in burgers] for topping in toppings]:  # noqa
    print(nested_meals)
# The above code is a nested list comprehension.

print()

for nested_meals in [[(burger, topping ) for topping in toppings] for burger in burgers]:  # noqa
    print(nested_meals)
