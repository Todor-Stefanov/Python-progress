day = input()
price = 0
if day == "Monday" or day == "Tuesday" or day == "Friday":
    price = 12
    print(price)
if day == "Wednesday" or day == "Thursday":
    price = 14
    print(price)
if day == "Saturday" or day == "Sunday":
    price = 16
    print(price)

