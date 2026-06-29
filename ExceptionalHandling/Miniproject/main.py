try:
    filename = input("Enter the file name: ") + ".txt"

    file = open(filename, "r")

    total_items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in file:

        line = line.strip()

        if line == "":
            continue

        data = line.split()

        if data[0] == "Discount":
            discount = int(data[1])

        elif data[1] == "Free":
            free_items += 1

        else:
            total_items += 1
            amount += int(data[1])

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", amount - discount)

    file.close()

except FileNotFoundError:
    print("File not found.")

except ValueError:
    print("Invalid data in file.")

except Exception as e:
    print("Error:", e)