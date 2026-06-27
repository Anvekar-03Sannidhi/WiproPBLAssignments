# Given 2 non negative values, print true iof they have same last digit

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 % 10 == num2 % 10:
    print("True")
else:   
    print("False")