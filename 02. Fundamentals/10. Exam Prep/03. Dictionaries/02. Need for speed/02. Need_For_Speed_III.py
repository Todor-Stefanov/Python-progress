n = int(input())  # number of cars that can be obtained

car_dict = {}
for i in range(n):
    car_input = input().split("|")
    car, mileage, fuel = car_input
    if car not in car_dict:
        car_dict[car] = {}
        car_dict[car]["m"] = int(mileage)
        car_dict[car]["fuel"] = int(fuel)

command = input().split(" : ")

while command[0] != "Stop":
    if command[0] == "Drive":
        do, car, distance, fuel = command
        if int(fuel) <= car_dict[car]["fuel"]:
            car_dict[car]["m"] += int(distance)
            car_dict[car]["fuel"] -= int(fuel)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_dict[car]["m"] >= 100000:
                print(f"Time to sell the {car}!")
                del car_dict[car]
        else:
            print("Not enough fuel to make that ride")

    elif command[0] == "Refuel":
        do, car, fuel = command
        max = 75
        over_max_refuel = max - car_dict[car]["fuel"]
        if car_dict[car]["fuel"] + int(fuel) > max:
            car_dict[car]["fuel"] = max
            print(f"{car} refueled with {over_max_refuel} liters")
        else:
            car_dict[car]["fuel"] += int(fuel)
            print(f"{car} refueled with {fuel} liters")

    else:
        do, car, kilometers = command
        car_dict[car]["m"] -= int(kilometers)
        if car_dict[car]["m"] < 10000:
            car_dict[car]["m"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input().split(" : ")

for key, value in car_dict.items():
    current_nested_values = []
    for nested_key, nested_value in value.items():
        current_nested_values.append(nested_value)
    print(f"{key} -> Mileage: {current_nested_values[0]} kms, Fuel in the tank: {current_nested_values[1]} lt.")

