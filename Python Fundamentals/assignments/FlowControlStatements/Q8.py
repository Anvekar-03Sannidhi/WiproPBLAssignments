#WAP to print sum of all the digits of a given number

num = int(input("Enter a number:"))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("The sum of all the digits is:", sum) 