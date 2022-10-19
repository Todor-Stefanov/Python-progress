from collections import deque
food_for_day = int(input())
food_per_order = input().split(" ")
integer_food_per_order = list(map(int, food_per_order))
queue = deque()
food_per_order.reverse()
stack = []
for i in range(len(food_per_order)):
    queue.append(food_per_order.pop())


print(max(integer_food_per_order))

for i in range(len(queue)):
    current_order = int(queue.popleft())
    if current_order <= food_for_day:
        food_for_day -= current_order
    else:
        stack. append(current_order)
    if bool(stack):
        for j in range(len(queue)):
            current_order = int(queue.popleft())
            stack.append(current_order)
        break

if bool(stack):
    stack = list(map(str, stack))
    print(f"Orders left: {' '.join(stack)}")
else:
    print(f"Orders complete")
