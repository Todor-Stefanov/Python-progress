import re

sentence = input()
special_word = input()

regex = rf"\b{special_word}\b"

result = re.findall(regex, sentence, re.IGNORECASE)

print(len(result))