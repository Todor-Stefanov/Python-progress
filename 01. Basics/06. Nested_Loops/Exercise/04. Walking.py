target_steps = 10000
total_steps = 0
while total_steps < target_steps:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        break
    current_steps = int(command)
    total_steps += current_steps
difference = abs(total_steps - target_steps)
if total_steps >= target_steps:
    print("Goal reached! Great job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal!")