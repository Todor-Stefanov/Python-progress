import re

regex = r'(www\.[A-Za-z0-9-]+(\.[a-z]+)+([A-Za-z0-9-]+)*)'

while True:
    string = input()
    if not string:
        break

    matches = re.findall(regex, string)

    if len(matches) > 0:
        print(matches[0][0])

