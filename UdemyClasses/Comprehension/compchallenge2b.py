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
for loc in sorted(locations):
    leaves_to_destination_1 = []
    for leave in leaves:
        if loc in leaves[leave].values():
            leaves_to_destination_1.append((leave, locations[leave]))
        print(f"Locations leading to {loc}", end='\t')
        print(leaves_to_destination_1)

print()

print("List comprehension inside a for loop")
print("------------------------------------")
for loc in sorted(locations):
    leaves_to_destination_2 = [(leave, locations[leave]) for leave in leaves if loc in leaves[leave].values()]  # noqa
    print("Locations leading to {loc}", end='\t')
    print(leaves_to_destination_2)
print()

print("Nested Comprehension")
print("--------------------")
leaves_to_destination_3 = [[(leave, locations[leave]) for leave in leaves
                            if loc in leaves[leave].values()]
                           for loc in sorted(locations)]
print(leaves_to_destination_3)

print()
for index, loc in enumerate(leaves_to_destination_3):
    print("Locations leading to {index}", end='\t')
    print(loc)
