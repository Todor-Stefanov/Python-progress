day = input()

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday" or day == "Sunday":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        print("Working day")
    else:
        print("Weekend")
else:
    print("Error")
