from collections import nametuple

def multiple_values():
    MyTuple = nametuple("MyTulpe", ["name", "age", "car"])
    name = "Grevy"
    age = 51
    car = "Rivan"
    return MyTuple(name, age, car)

# Calling the function
result = multiple_values()
name = result.name
age = result.age
car = result.car

print(f"Name: {name}, Age: {age}, Car: {car}")
