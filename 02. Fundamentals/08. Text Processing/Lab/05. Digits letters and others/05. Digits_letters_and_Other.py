text = input()
digits = ""
letters = ""
chars = ""

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isupper() or ch.isupper(): # elif ch.isalpha()
        letters += ch
    else:
        chars += ch

print(digits)
print(letters)
print(chars)

# isalnum() - digits и letters