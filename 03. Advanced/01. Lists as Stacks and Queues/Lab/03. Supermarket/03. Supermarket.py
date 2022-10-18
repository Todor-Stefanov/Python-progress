from collections import deque
name = input()
queue = deque()
while name != "End":
    queue.append(name)
    if name == "Paid":
        queue.pop()
        for i in range(len(queue)):
            current_name = queue.popleft()
            print(current_name)
    name = input()
print(f"{len(queue)} people remaining.")



