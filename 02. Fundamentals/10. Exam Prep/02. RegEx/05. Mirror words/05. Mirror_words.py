import re

text = input()
regex = r"\@([A-Za-z]{3,})\@{2}([A-Za-z]{3,})\@|\#([A-Za-z]{3,})\#{2}([A-Za-z]{3,})\#"

matches = re.findall(regex, text)

mirror_matches = []
for i in range(len(matches)):
    if matches[i][0] != "":
        reversed_match = (matches[i][1])[::-1]
        if matches[i][0] == reversed_match:
            current_match = (matches[i][0], matches[i][1])
            mirror_matches.append(current_match)
    else:
        if matches[i][0] == "":
            reversed_match = (matches[i][3])[::-1]
            if matches[i][2] == reversed_match:
                current_match = (matches[i][2], matches[i][3])
                mirror_matches.append(current_match)

if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")
else:
    print(f"No word pairs found!")
output_list = []
if len(mirror_matches) > 0:
    print("The mirror words are:")
    for i in range(len(mirror_matches)):
        wordOne, wordTwo = mirror_matches[i]
        output_list.append(f"{wordOne} <=> {wordTwo}")
    print(', '.join(output_list))
else:
    print("No mirror words!")



