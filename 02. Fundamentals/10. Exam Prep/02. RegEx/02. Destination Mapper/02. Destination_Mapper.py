import re

text = input()
regex = r"=([A-Z][A-Za-z]{2,})=|\/([A-Z][A-Za-z]{2,})\/"
matches = re.findall(regex, text)

match_list = []
for i in range(len(matches)):
    destination, empty = matches[i]
    if destination == '':
        match_list.append(empty)
    else:
        match_list.append(destination)

travel_points = 0
for match in match_list:
    travel_points += len(match)


print(f"Destinations: {', '.join(match_list)}")
print(f"Travel Points: {travel_points}")
