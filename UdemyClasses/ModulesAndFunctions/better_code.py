"""This is a global variable that is used to store the area of a square."""
area = 0
length = 30


def area_of_square(length: float) -> float:
    """This is a function called area_of_square with 0 arguments."""
    return length * length


area = area_of_square(30)
print(f'The area is {area}')
