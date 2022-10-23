number_of_cars = int(input())

cars_in = set()
cars_out = set()

for i in range(number_of_cars):
    direction_car = tuple(input().split(', '))
    direction, car = direction_car
    if direction == "IN":
        cars_in.add(car)
        if car in cars_out:
            cars_out.remove(car)
    else:
        cars_out.add(car)

cars_left_in = cars_in - cars_out
if len(cars_left_in) != 0:
    for g in cars_left_in:
        print(g)
else:
    print("Parking Lot is Empty")
