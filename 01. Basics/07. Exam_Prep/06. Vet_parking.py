day_of_the_week = int(input())
hours_of_the_day = int(input())
cost_for_all_period = 0

for day in range(1, day_of_the_week + 1):
    current_cost = 0
    for hour in range(1, hours_of_the_day + 1):
        if day % 2 == 0:
            if hour % 2 != 0:
                cost_for_all_period += 2.50
                current_cost += 2.50
            else:
                cost_for_all_period += 1
                current_cost += 1
        elif day % 2 != 0:
            if hour % 2 == 0:
                cost_for_all_period += 1.25
                current_cost += 1.25
            else:
                cost_for_all_period += 1
                current_cost += 1  # suhranqva stoinostite samo ot tekushtotot zavurtane. toest samo ot tozi den

    print(f"Day: {day} - {current_cost:.2f} leva")  # mejdu ediniq i drugiq for se pravi tozi print

print(f"Total: {cost_for_all_period:.2f} leva")
