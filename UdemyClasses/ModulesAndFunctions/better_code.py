"""This is a global variable that is used to store the area of a square."""
area = 0
length = 30


def area_of_square(length: float) -> float:
    """This is a function called area_of_square with 0 arguments."""
    return length * length


if __name__ == '__main__':
    area = area_of_square(30)
    print(f'The area is {area}')

    print(f'in better_code.py, __name__ is {__name__}')
