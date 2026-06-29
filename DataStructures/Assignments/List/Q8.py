# WAP to remove the first occurence of a specified element of the list

my_list = [10, 20, 30, 20, 40]
val = 20

if val in my_list:
    my_list.remove(val)
    print("Updated list:", my_list)
else:
    print("Value not found in list")
