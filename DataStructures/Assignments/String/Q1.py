# Write a program to count the number of upper and lower case letters in a String.

text = "Hello World!"
upper_cnt = sum(1 for c in text if c.isupper())
lower_cnt = sum(1 for c in text if c.islower())
print("Uppercase letters:", upper_cnt)
print("Lowercase letters:", lower_cnt)

