budget = float(input())
statists = int(input())
clothing_price = float(input())

dekor = 10 / 100 * budget

if statists > 150:
    clothing_price = clothing_price * statists - (clothing_price * statists * 1 / 10)
    sum_all = dekor + clothing_price
else:
    clothing_price = clothing_price * statists
    sum_all = dekor + clothing_price

if sum_all <= budget:
    print("Action!")
    print(f'Wingard starts filming with {budget - sum_all:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {sum_all - budget:.2f} leva more.')