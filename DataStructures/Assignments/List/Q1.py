#WAP to create a list of 5 ints and display list items. Access individual elements through index

list = [10, 20, 30, 40, 50]
print("List items:")
for item in list:
    print(item)
print("\nAccessing individual elements through index:")
for i in range(len(list)):
    print(f"Element at index {i}: {list[i]}")