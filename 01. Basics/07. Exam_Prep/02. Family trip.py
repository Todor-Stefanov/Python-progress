budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_za_nepredvidimost = int(input())

if nights > 7:
    price_per_night = price_per_night - (price_per_night * 5 / 100)

nepredvidimost = budget * percent_za_nepredvidimost / 100
price_for_vacation = price_per_night * nights + nepredvidimost

money_left = abs(budget - price_for_vacation)

if budget < price_for_vacation:
    print(f"{money_left:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")


