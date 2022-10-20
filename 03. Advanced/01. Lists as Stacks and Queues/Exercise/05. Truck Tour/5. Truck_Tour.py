from collections import deque
number_of_pumps = int(input())



petrol_pumps = deque()
distance_between_pumps = deque()
for i in range(number_of_pumps):
    petrol_distance = input().split(" ")
    petrol_pumps.append(petrol_distance[0])
    distance_between_pumps.append(petrol_distance[1])


start_pump = 0
while True:
    counter = 0
    value = 0
    petrol_in_tank = 0
    while petrol_in_tank >= 0:
        if counter == number_of_pumps:
            break
        counter += 1
        petrol_in_tank += int(petrol_pumps[value]) - int(distance_between_pumps[value])
        value += 1
    if counter == number_of_pumps:
        break
    else:
        negative = petrol_pumps.popleft()
        petrol_pumps.append(negative)

        negative2 = distance_between_pumps.popleft()
        distance_between_pumps.append(negative2)
    start_pump += 1

print(start_pump)