# Create a comprehension that returns a list of all the LOCations that have an leave to the forest.  # noqa
# The list should contain the description of each LOCation, if it's possible to get to the forest from there.  # noqa
#
# The forest is LOCation 5 in the LOCations dictionary
# The leaves for each LOCation are represented by the leaves dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.  # noqa
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.  # noqa
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.  # noqa
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.  # noqa
# Each tuple consists of the LOCation number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the LOCations that lead to each of the  # noqa
# other LOCations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the LOCations dictionary.  # noqa


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

LOC = 1
forest = [locations[leave] for leave in leaves if LOC in leaves[leave].values()]
print(forest)

forest = []
for leave in leaves:
    if LOC in leaves[leave].values():
        forest.append(locations[leave])
print(forest)

print()

# for loc in sorted(locations):
#     forest = [f"{leave}, {locations[leave]}" for leave in leaves if LOC in leaves[leave].values()]  # noqa
#     print(f"Locations leading to {loc}", end='\t')
#     print(forest)
for loc in sorted(locations):
    forest = []
    for leave in leaves:
        if LOC in leaves[leave].values():
            forest.append((leave, locations[leave]))
    print(f"Locations leading to {loc}", end='\t')
    print(forest)
