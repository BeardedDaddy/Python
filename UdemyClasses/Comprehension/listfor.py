"""
This script prompts the user to enter a number. It then squares each number in a predefined list,
and prints the square of the number entered by the user.

The script uses a for loop to square each number in the list, and the `index`
method to find the position
of the user's number in the list.

This script prints the name of the file it's running from at the start.
"""
print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number, and I'll tell you which one is squared. "))  # noqa

squares = []
for number in numbers:
    squares.append(number ** 2)

index_pos = numbers.index(number)
print(squares[index_pos])
