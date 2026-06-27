# Project 1

dist = float(input("How far would you like to travel in miles? : "))

if dist < 3:
    print("I suggest Bicycle for you")
elif dist > 3 and dist < 300:
    print("I suggest Motor-Cycle for you")
else:
    print("I suggest Super-Car for you")