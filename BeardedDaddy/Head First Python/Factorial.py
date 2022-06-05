Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num = int(input("Enter any number : "))
Enter any number : 5

def cal_factorial(num):
    factorial = 1
    if num == 0 or num == 1:
        return 1
    for i in range(1, num+1):
        factorial = factorial * 1
    return factorial


output = cal_factorial(num)
print("Factorial of number ", num, "is : ", output)