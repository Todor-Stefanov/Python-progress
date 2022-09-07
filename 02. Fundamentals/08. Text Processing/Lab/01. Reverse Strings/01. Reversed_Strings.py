text = input()
while text != "end":
    rev = reversed(text)
    reversed_text = "".join(rev) # reversed_text = text[::-1]
    print(reversed_text)
    text = input()
