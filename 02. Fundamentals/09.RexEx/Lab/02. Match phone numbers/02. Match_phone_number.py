import re

text = input()
matches = re.findall("(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b", text)
print(", ".join(matches))
