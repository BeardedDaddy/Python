from Calcu import *

a = 9
b = 7

c = multi(a,b)

print(c)

print("Hello Visual Studio")

import sys
from math import cos, radians

# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    return ' ' * int(20 * cos(radians(x)) +20) + 'o'

make_dot_string(90)
'                o'
make_dot_string(180)
'o'
make_dot_string(135)
'  o'

