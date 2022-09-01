targets = input().split(" ")
targets = list(map(int, targets))
command = input()
while command != "End":
    explode = command.split(" ")
    current_command = explode[0]
    index = int(explode[1])
    if current_command == "Shoot" and index >= 0 and index < len(targets):
        power = int(explode[2])
        targets[index] -= power
        current_target = targets[index]
        if targets[index] <= 0:
            targets.remove(current_target)
        else:
            targets[index] = current_target
    elif current_command == "Add":
        value = int(explode[2])
        if index >= 0 and index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif current_command == "Strike":
        radius = int(explode[2])
        if index - radius >= 0 and index + radius < len(targets):
            targets = targets[:index - radius] + targets[index + radius + 1:]
            # targets.remove(targets[index - radius])
        else:
            print("Strike missed!")
    command = input()

print(*targets, sep="|")
