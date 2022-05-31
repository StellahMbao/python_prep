from calendar import week


week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week_days[-1])

print(week_days[2:4])
#the forth index isn't picked
#list fundtions
lucky_numbers = [3, 10, 9, 100, 22, 620, 490, 11]
#extending lists
# week_days.extend(lucky_numbers)
print(week_days)
week_days.append('Caturday')
print(week_days)
week_days.insert(2, "Appleday")
print(week_days)
week_days.remove('Caturday')
print(week_days)

# print(week_days.clear())
print(week_days.pop())
print(lucky_numbers.sort)