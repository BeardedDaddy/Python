# List are you use to store multiple items in a single variable
# Example: thislist = ["apple", "banana", "oranges"]
#print(thislist)

a = [3, 10, -1]
print(a)
a.append(1)
#Appending will add 1 to the end of existing list
print(a)
a.append("hello")
print(a)
a.append([1, 2])
print(a)
a.pop()
print(a)
a.pop()
print(a)
print(a[0])
print(a[3])
a[0] = 100
print(a)
b =['apple', 'banana', 'microsoft']
print(b)
#Swapping the elements in a list
temp = b[0]
# Make a new variable called temp
b[0] = b[2]
# Have 0 variable refer to the 2 variable
b[2] = temp
# Have the 2 variable refer to the temp variable
print(b)
