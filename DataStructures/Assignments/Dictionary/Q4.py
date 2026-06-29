# Write a program to iterate over a dictionary using for loop and print the keys alone, values alone
# and both keys and values.

dictionary = {"name": "Alice", "age": 25, "city": "Pune"}

print("Keys:")
for key in dictionary:
    print(key)

print("\nValues:")
for value in dictionary.values():
    print(value)

print("\nKeys and Values:")
for key, value in dictionary.items():
    print(key, ":", value)
