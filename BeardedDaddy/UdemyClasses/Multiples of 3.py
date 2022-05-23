
total = 0
for i in list(range(1, 100)):
    if i % 3 and 5 == 0:
        total += i
print(total)

total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)

a = ['apple', 'banana', 'microsoft']
for element in a:
    print(element)
    
for i in range(len(a)):
    for j in range(i + 1):
        print(a[i])

