flower = input()
flower_number = int(input())
budget = int(input())

price = 0

if flower == "Roses":
    if flower_number <= 80:
        price = 5
    else:
        price = 5 - (5 * 10 / 100)
elif flower == "Dahlias":
    if flower_number <= 90:
        price = 3.80
    else:
        price = 3.80 - (3.80 * 15 / 100)
elif flower == "Tulips":
    if flower_number <= 80:
        price = 2.80
    else:
        price = 2.80 - (2.80 * 15 / 100)
elif flower == "Narcissus":
    if flower_number < 120:
        price = 3 + (3 * 15 / 100)
    else:
        price = 3
elif flower == "Gladiolus":
    if flower_number < 80:
        price = 2.50 + (2.50 * 20 / 100)
    else:
        price = 2.50
overall_price = flower_number * price
difference = abs(budget - overall_price)
if budget >= overall_price:
    print(f"Hey, you have a great garden with {flower_number} {flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")




