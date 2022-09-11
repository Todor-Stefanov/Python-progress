import re

names = input().split(", ")
name_list = [name for name in names]


first_letter_of_name_regex = r"[A-Z]"
small_letters_of_name_regex = r"[a-z]"
numbers_regex = r"[0-9]"
racers = {}
command = input()
while command != "end of race":
    current_name = ''
    distance = 0
    first_letter = re.findall(first_letter_of_name_regex, command)
    small_letters = re.findall(small_letters_of_name_regex, command)
    numbers = re.findall(numbers_regex, command)

    current_name += first_letter[0]
    for i in small_letters:
        current_name += i

    if current_name in name_list:
        for j in numbers:
            distance += int(j)
        if current_name not in racers:
            racers[current_name] = distance
        else:
            racers[current_name] += distance

    command = input()

sorted_racers = {k: v for k, v in sorted(racers.items(), key=lambda item: item[1])} # sorts dict po values

racers_list = []

for key in sorted_racers.items():
    racers_list.append(key)

racers_list.reverse()
print(f"1st place: {racers_list[0][0]}")
print(f"2nd place: {racers_list[1][0]}")
print(f"3rd place: {racers_list[2][0]}")
