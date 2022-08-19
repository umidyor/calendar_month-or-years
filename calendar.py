import calendar

a = int(input("First enter the year to find out which month of the year it is>>> "))
y = input(f"Now enter the name or order number of the desired month of the {a}th year >>> ")

for i in y:
    if y.lower() == "january" or y == "1":
        print(calendar.month(a, 1))
        break
    if y.lower() == "february" or y == "2":
        print(calendar.month(a, 2))
        break
    if y.lower() == "march" or y == "3":
        print(calendar.month(a, 3))
        break
    if y.lower() == "april" or y == "4":
        print(calendar.month(a, 4))
        break
    if y.lower() == "may" or y == "5":
        print(calendar.month(a, 5))
        break
    if y.lower() == "june" or y == "6":
        print(calendar.month(a, 6))
        break
    if y.lower() == "july" or y == "7":
        print(calendar.month(a, 7))
        break
    if y.lower() == "august" or y == "8":
        print(calendar.month(a, 8))
        break
    if y.lower() == "september" or y == "9":
        print(calendar.month(a, 9))
        break
    if y.lower() == "november" or y == "10":
        print(calendar.month(a, 10))
        break
    if y.lower() == "october" or y == "11":
        print(calendar.month(a, 11))
        break
    if y.lower() == "december" or y == "12":
        print(calendar.month(a, 12))
        break

###############################################
june = calendar.month(2020, 6, w = 3, l=2)   #It's just spacing the days of the calendar table!
print(june)

