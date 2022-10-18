text = list(input())
stack = []

for i in range(len(text)):
    text_last_letter = text.pop()
    stack.append(text_last_letter)
print("".join(stack))
