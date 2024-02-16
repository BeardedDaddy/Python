import timeit

setup = """\
gc.enable()
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
"""
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
          4: {"N": 1, "W": 2, "Q": 0}}


def NESTED_LOOP():
    result = []
    for loc in sorted(locations):
        leaves_to_destination_1 = []
        for leave in leaves:
            if loc in leaves[leave].values():
                leaves_to_destination_1.append((leave, locations[leave]))
        result.append(leaves_to_destination_1)
    # print the result before returning
    for x in result:
        pass
    
    return result

# The backslash at the end of line 19 is because we don't want to start our
# string with a blank space and a backslash acts as a line continuation
# character avoids that issue.
# gc stands for garbage collection.


def LOOP_COMP():
    result = []
    for loc in sorted(locations):
        leaves_to_destination_2 = [(leave, locations[leave]) for leave in leaves if loc in leaves[leave].values()]  # noqa
        result.append(leaves_to_destination_2)
    # print the result before returning
    for x in result:
        pass

    return result


def NESTED_COMP():
    leaves_to_destination_3 = [[(leave, locations[leave]) for leave in leaves
                                if loc in leaves[leave].values()]
                               for loc in sorted(locations)]
    # print the result before returning
    for x in leaves_to_destination_3:
        pass

    return leaves_to_destination_3


def NESTED_GEN():
    leaves_to_destination_3 = ([(leave, locations[leave]) for leave in leaves
                                if loc in leaves[leave].values()]
                               for loc in sorted(locations))
    # print the result before returning
    for x in leaves_to_destination_3:
        pass

    return leaves_to_destination_3

# In this module we are using the timeit module. We are converting the list
# comprehensions into strings by put them in triple quotes.
# In the above code I removed the print statements and replaced them with result.  # noqa


print(NESTED_LOOP())
print(LOOP_COMP())
print(NESTED_COMP())
result_1 = timeit.timeit(NESTED_LOOP, setup, number=1000)
result_2 = timeit.timeit(LOOP_COMP, setup, number=1000)
result_3 = timeit.timeit(NESTED_COMP, setup, number=1000)
result_4 = timeit.timeit(NESTED_GEN, setup, number=1000)
print(f"Nested loop:\t{result_1}")
print(f"LOOP_COMP:\t{result_2}")
print(f"Nested_COMP:\t{result_3}")
print(f"Nested_GEN:\t{result_4}")
