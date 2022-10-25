"""
Learning how to work with binary files bytes andbytearrays.
"""

# EQUATION = bytes ((207, 128, 114, 194, 178))
EQUATION = b'\xcf\x80r\xc2\xb2'
print(EQUATION)
print(type(EQUATION))
print(len(EQUATION))

for b in EQUATION:
    print(b, end=',')
print()
