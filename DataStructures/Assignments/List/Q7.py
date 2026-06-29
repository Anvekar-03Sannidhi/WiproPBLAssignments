# WAP to remove the element from the specified idx of a list

my_list = [10, 20, 30, 40, 50]
idx = 2

if 0 <= idx < len(my_list):
    removed_value = my_list.pop(idx)
    print("Removed value:", removed_value)
    print("Updated list:", my_list)
else:
    print("Index out of range")
