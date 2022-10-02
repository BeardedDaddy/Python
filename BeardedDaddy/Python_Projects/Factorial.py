

num = int(input("Enter any number : "))

def cal_factorial(num):
    factorial = 1
    if num == 0 or num == 1:
        return 1
    for i in range(1, num+1):
        factorial = factorial * num
    return factorial


output = cal_factorial(num)
print("Factorial of number ", num, "is : ", output)
