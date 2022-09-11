import re

regex = r"\b_{1}([a-zA-Z0-9]+)\b"

text = input()

matches = re.findall(regex, text)

print(",".join(matches))