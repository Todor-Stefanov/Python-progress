open = ["{", "(", "["]
closed = ["}", ")", "]"]
paren = input()
stack = []

bool = 0
for i in range(len(paren)):
    if paren[i] in open:
        stack.append(paren[i])
    elif paren[i] in closed:
        pos = closed.index(paren[i])
        if (len(stack) > 0) and (open[pos] == stack[len(stack) - 1]):
            stack.pop()
        else:
            bool = 1

if len(stack) == 0 and bool == 0:
    print("YES")
else:
    print("NO")
