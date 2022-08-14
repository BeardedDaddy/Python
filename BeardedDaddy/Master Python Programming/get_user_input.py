#print('An example of using the input() function')
#name = input ('Enter your name: ')
#print('Type:' , type(name))
#print('Your name is: ', name)

price = input('Enter the price: ')
quantity = input('Enter the quantity: ')

total_value = float(price) * int(quantity)
# Here we converted the data type from string to intergers.

print('Total_value: $', total_value)
