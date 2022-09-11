import re

regex = r'\d+'

while True:
    string = input()
    if not string:
        break

    matches = re.findall(regex, string)

    if len(matches) > 0:
        print(" ".join(matches), end=" ")

