num_wagon = int(input())
train = [0 for i in range(num_wagon)]

command = input()

while command != "End":
    explode = command.split(" ")
    current_command = explode[0]
    if current_command == "add":
        num_people = int(explode[1])
        train[-1] += num_people

    elif current_command == "insert":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] += num_people
    elif current_command == "leave":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] -= num_people
    command = input()

print(train)
