command = input()
cities_dict = {}
while command != "Sail":
    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in cities_dict:
        cities_dict[city] = {}
        cities_dict[city]["population"] = population
        cities_dict[city]["gold"] = gold
    else:
        cities_dict[city]["population"] += population
        cities_dict[city]["gold"] += gold
    command = input()

event = input()
while event != "End":
    event = event.split("=>")
    event_name = event[0]
    town = event[1]
    if event_name == "Plunder":
        people = int(event[2])
        gold = int(event[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        #for key in cities_dict.keys():
            #if key != town:
                #continue
            #for nested_key, nested_value in value.items():
                #if nested_key == "population":
                    #nested_value -= people
                    #cities_dict[key]["population"] = nested_value
                #elif nested_key == "gold":
                    #nested_value -= gold
                    #cities_dict[key]["gold"] = nested_value

        cities_dict[town]['population'] -= people
        if cities_dict[town]["population"] == 0:
            del cities_dict[town]
            print(f"{town} has been wiped off the map!")


        else:
            cities_dict[town]['gold'] -= gold
            if cities_dict[town]["gold"] == 0:
                del cities_dict[town]
                print(f"{town} has been wiped off the map!")


    elif event_name == "Prosper":
        gold = int(event[2])
        if gold >= 0:
            cities_dict[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

    event = input()

if len(cities_dict.keys()) > 0:
    print(f"Ahoy, Captain! There are {len(cities_dict.keys())} wealthy settlements to go to:")
    for key in cities_dict.keys():
        print(f"{key} -> Population: {cities_dict[key]['population']} citizens, Gold: {cities_dict[key]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

