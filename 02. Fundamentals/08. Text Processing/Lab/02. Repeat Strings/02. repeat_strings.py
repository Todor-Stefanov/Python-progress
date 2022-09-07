words = input().split(" ")
output = ""
for word in words:
    lenght = len(word)
    output += word * lenght

print(output)