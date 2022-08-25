import sys

max_number = -sys.maxsize

command = input()

while command != "Stop":
    num = int(command)
    if num > max_number:
        max_number = num
    command = input()

print(max_number)