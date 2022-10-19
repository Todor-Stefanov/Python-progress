numbers = input().split(" ")
stack = []

for i in range(len(numbers)):
    last_number = numbers.pop()
    stack.append(last_number)

print(" ".join(stack))