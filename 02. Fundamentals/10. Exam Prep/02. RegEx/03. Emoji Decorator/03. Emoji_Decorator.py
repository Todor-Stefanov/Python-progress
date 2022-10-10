import re

regex_text = r"\:\:[A-Z][a-z]{2,}\:\:|\*\*[A-Z][a-z]{2,}\*\*"
text = input()
regex_digits = r"[0-9]"
matches = re.findall(regex_text, text)
digit_matches = re.findall(regex_digits, text)
cool_number = 1

for digit in digit_matches:
    cool_number *= int(digit)

print(f"Cool threshold: {cool_number}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for match in matches:
    sum = 0
    regex_emoji = r"([A-Z][a-z]{2,})"
    emoji_match = re.findall(regex_emoji, match)
    for letter in emoji_match[0]:
        sum += ord(letter)
    if sum >= cool_number:
        print(match)


