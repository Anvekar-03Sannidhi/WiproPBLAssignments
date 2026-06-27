# Project 2

costperHr = 0.51
costperDay = costperHr * 24
costperWeek = costperDay * 7
costperMonth = costperDay * 30

daysWith918 = 918 / costperDay

print("Cost to operate 1 server per day: $", round(costperDay, 2))
print("Cost to operate 1 server per week: $", round(costperWeek, 2))
print("Cost to operate 1 server per month: $", round(costperMonth, 2))
print("Number of days 1 server can can operate with $918: ", round(daysWith918, 2))