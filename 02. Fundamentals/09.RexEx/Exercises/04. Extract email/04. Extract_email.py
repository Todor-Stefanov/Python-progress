import re

text = input()
regex = r"( |^)\b([A-Za-z0-1]+([-._][A-Za-z0-1]+)?@(([a-zA-Z])+(([-][a-zA-Z]+)*))(\.(([a-zA-Z])+(([-][a-zA-Z]+)*)))+)\b"

matches = re.findall(regex, text)


for i in range(len(matches)):
    print(matches[i][1])
