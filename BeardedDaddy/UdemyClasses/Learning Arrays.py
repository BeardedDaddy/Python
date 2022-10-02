from array import *

vals = array('i', [5,9,8,4,2])

NewArray = array(vals.typecode, (a*a for a in vals))
#for i in NewArray:
#    print(i)

i = 0

while i<len(NewArray):
    print(NewArray[i])
    i +=1
