stack = []
number = int(input())
integer_stack = []
query = input()
number_to_push = ""
for i in range(number):
    stack = list(map(int, stack))
    if query[0] == "1":
        for c in range(len(query)):
            if c > 1:
                number_to_push += query[c]

        stack.append(number_to_push)
        number_to_push = ""
    elif query[0] == "2":
        if len(stack) != 0:
            stack.pop()
    elif query[0] == "3":
        print(max(stack))
    elif query[0] == "4":
        print(min(stack))

    if i == number - 1:
        break
    query = input()

stack.reverse()
stack = list(map(str, stack))
print(", ".join(stack))