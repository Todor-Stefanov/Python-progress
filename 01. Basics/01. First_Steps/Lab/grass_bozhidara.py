yards = float(input())

price = yards * 7.61

discount = price * 18 / 100
final_price = price - discount

print(f'The final price is: {final_price} lv.')

print(f'The discount is: {discount} lv.')
