import sys

# Read command line arguments
string1 = sys.argv[1]
string2 = sys.argv[2]
string3 = sys.argv[3]

# strings -> lists
liked = string1.split("-")
disliked = string2.split("-")
numbers = string3.split("-")

happiness = 0

for num in numbers:
    if num in liked:
        happiness += 1
    elif num in disliked:
        happiness -= 1

print("Final Happiness:", happiness)