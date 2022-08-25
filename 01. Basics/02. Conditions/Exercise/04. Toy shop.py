excursion_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
teddies_number = int(input())
minions_number = int(input())
lorries_number = int(input())

toys_number = puzzles_number + dolls_number + teddies_number + minions_number + lorries_number
sum_price = (puzzles_number * 2.60) + (dolls_number * 3.00) + (teddies_number * 4.10) + (minions_number * 8.20) + (lorries_number * 2.00)

if toys_number >= 50:
    sum_price = sum_price - (sum_price * 25 / 100)
    rent = 10 / 100 * sum_price
else:
    rent = 10 / 100 * sum_price

final_price = sum_price - rent

if final_price >= excursion_price:  # !!а не само >
    money_left = final_price - excursion_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = excursion_price - final_price
    print(f'Not enough money! {money_needed:.2f} lv needed.')
