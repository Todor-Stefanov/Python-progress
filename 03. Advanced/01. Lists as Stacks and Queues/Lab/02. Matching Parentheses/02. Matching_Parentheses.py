from collections import deque
math = input()
queue = deque(math)
stack = []

for i in range(len(math)):
    if math[i] == "(":
        stack.append(i)
    elif math[i] == ")":
        stack_starting = stack.pop()
        print(math[stack_starting:i+1])  # да принтира всичко от старт индекса до i+1

