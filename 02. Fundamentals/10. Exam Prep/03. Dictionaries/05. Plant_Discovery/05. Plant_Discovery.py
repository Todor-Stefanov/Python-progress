n = int(input())

plant_dict = {}
for i in range(n):
    info = input().split("<->")
    plant, rarity = info
    if plant not in plant_dict:
        plant_dict[plant] = {}
        plant_dict[plant]["rarity"] = int(rarity)
        plant_dict[plant]["rating"] = []
    else:
        plant_dict[plant]["rarity"] = int(rarity)

command = input().split(': ')
while command[0] != "Exhibition":
    if command[0] == "Rate":
        current_plant, rating = command[1].split(" - ")
        if current_plant not in plant_dict:
            print("error")
        else:
            plant_dict[current_plant]["rating"].append(int(rating))

    elif command[0] == "Update":
        current_plant, new_rarity = command[1].split(" - ")
        if current_plant not in plant_dict:
            print("error")
        else:
            plant_dict[current_plant]["rarity"] = int(new_rarity)
    else:
        current_plant = command[1]
        if current_plant not in plant_dict:
            print("error")
        else:
            plant_dict[current_plant]["rating"].clear()

    command = input().split(': ')

print("Plants for the exhibition:")

for key, value in plant_dict.items():
    nested_values = []
    for nestedkey, nestedvalue in value.items():
        nested_values.append(nestedvalue)
    if len(nested_values[1]) == 0:
        average_rating = 0
    else:
        sum = 0
        for x in nested_values[1]:
            sum += x
        average_rating = sum / len(nested_values[1])

    print(f"- {key}; Rarity: {nested_values[0]}; Rating: {average_rating:.2f}")










