string = input()

leftover = 0
for i in range(len(string)):
    if string[i] == ">":
        digit = string[i+1].isdigit()
        if digit > 1 and string[i + 2] == ">":
            string = string.replace(str(digit), "")
            leftover += digit - 1
        else:
            digit += leftover
            for ch in range(digit):
                string = string.replace(str(ch), "")

print(string)





