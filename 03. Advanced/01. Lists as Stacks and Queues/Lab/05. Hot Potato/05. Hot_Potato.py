from collections import deque
names = input().split(" ")
tosses = int(input())
queue = deque(names)

for i in range(tosses):
    if i == len(queue):
        i = 0
    if len(queue) == 1:
        break
    current_player = queue[i]












