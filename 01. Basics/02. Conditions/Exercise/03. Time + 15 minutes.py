import math

hour = int(input())
minute = int(input())

minute = minute + 15

if minute >= 60:
    hour = hour + 1
    minute = 0 + minute % 60
    if hour + 1 > 23:
        hour = 0


if minute < 10:
    print(f'{hour}:0{minute}')
else:
    print(f'{hour}:{minute}')
