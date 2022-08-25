budget = float(input())

product_name = input()
product_price_counter = 0
product_number_counter = 0

while product_name != "Stop":
    product_price = float(input())
    product_number_counter += 1
    if product_number_counter % 3 == 0:
        product_price = product_price / 2
    product_price_counter += product_price
    current_budget = budget - product_price_counter
    if current_budget < 0:
        print("You don't have enough money!")
        print(f"You need {abs(current_budget):.2f} leva!")
        break
    product_name = input()

if current_budget > 0:
    print(f"You bought {product_number_counter} products for {product_price_counter:.2f} leva.")
