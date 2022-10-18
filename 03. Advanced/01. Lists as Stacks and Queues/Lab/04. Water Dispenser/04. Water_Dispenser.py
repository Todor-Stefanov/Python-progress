from collections import deque
water = int(input())
people = input()
queue = deque()

while people != "Start":
    queue.append(people)
    people = input()
command = input()
refill = ""
while command != "End":
    if "refill" in command:
        for i in command:
            if i.isdigit():
                refill += i
        reliters = int(refill)
        water += reliters
        refill = " "

    else:
        current_person = queue.popleft()
        liters = int(command)
        if liters <= water:
            print(f"{current_person} got water")
            water -= liters
        else:
            print(f"{current_person} must wait")
    command = input()
print(f"{water} liters left")