# Convert all comprehensions in the previous challenge to for loops

We started off by creating a list comprehension from a for loop, this challenge is to go the other way: convert each of the comprehensions in the previous challenge into a for loop that produces the same result

LOC = 1
forest = [locations[exit] for exit in exits if LOC in exits[exit].values()]
print(forest)

for loc in sorted(locations):
    forest = [f"{exit}, {locations[exit]}" for exit in exits if LOC in exits[exit].values()]  # noqa
    print(f"Locations leading to {loc}", end='\t')
    print(forest)
