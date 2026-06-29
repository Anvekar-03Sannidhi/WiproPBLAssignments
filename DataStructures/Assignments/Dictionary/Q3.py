# Write a program to check if a given key already exists in a dictionary.

dictionary = {"a": 1, "b": 2, "c": 3}
key_to_check = "b"

if key_to_check in dictionary:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
