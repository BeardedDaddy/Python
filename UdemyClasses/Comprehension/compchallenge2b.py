import timeit

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",  # noqa
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

leaves = {0: {"Q": 0},
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
          2: {"N": 5, "Q": 0},
          3: {"W": 1, "Q": 0},
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S": 1, "Q": 0}}

print("Nested for loops")
print("----------------")
NESTED_LOOP = """\
for loc in sorted(locations):
    leaves_to_destination_1 = []
    for leave in leaves:
        if loc in leaves[leave].values():
            leaves_to_destination_1.append((leave, locations[leave]))
        print(f"Locations leading to {loc}", end='\t')
        print(leaves_to_destination_1)
"""
# The backslash at the end of line 19 is because we don't want to start our
# string with a blank space and a backslash acts as a line continuation
# character avoids that issue.
print()

print("List comprehension inside a for loop")
print("------------------------------------")
LOOP_COMP = """\
for loc in sorted(locations):
    leaves_to_destination_2 = [(leave, locations[leave]) for leave in leaves if loc in leaves[leave].values()]  # noqa
    print("Locations leading to {loc}", end='\t')
    print(leaves_to_destination_2)
"""
print()

print("Nested Comprehension")
print("--------------------")
NESTED_COMP = """\
leaves_to_destination_3 = [[(leave, locations[leave]) for leave in leaves
                            if loc in leaves[leave].values()]
                           for loc in sorted(locations)]
for index, loc in enumerate(leaves_to_destination_3):
    print("Locations leading to {index}", end='\t')
    print(loc)
"""
# In this module we are using the timeit module. We are converting the list
# comprehensions into strings by put them in triple quotes.

result_1 = timeit.timeit(NESTED_LOOP)
print(f"Nested loop:\t{result_1}")
