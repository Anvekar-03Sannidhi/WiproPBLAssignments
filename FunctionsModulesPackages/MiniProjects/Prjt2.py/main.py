import mymodule

name = input("Enter your name: ")

if mymodule.ispalindrome(name):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")


print("No of vowels:", mymodule.count_the_vowels(name))

frequency = mymodule.frequency_of_letters(name)

print("Frequency of letters:")

for key in frequency:
    print(key, "-", frequency[key], end=", ")
