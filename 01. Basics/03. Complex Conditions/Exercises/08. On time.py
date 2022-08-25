hour_of_examine = int(input())
minutes_of_examine = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())
time_of_examine = hour_of_examine * 60 + minutes_of_examine
time_of_arriving = hour_of_arriving * 60 + minutes_of_arriving
if time_of_arriving > time_of_examine:
    print('Late')
elif time_of_examine - 30 <= time_of_arriving <= time_of_examine:
    print("On time")
else:
    print("Early")

difference = abs(time_of_arriving - time_of_examine)

if time_of_examine - 60 < time_of_arriving < time_of_examine:
    print(f"{difference} minutes before the start")
elif time_of_arriving <= time_of_examine - 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")

elif time_of_examine < time_of_arriving < time_of_examine + 60:
    print(f'{difference} minutes after the start')

elif time_of_arriving >= time_of_examine + 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start") #or 02d

