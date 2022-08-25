product = input()
town = input()
quantity = float(input())

price = 0

if town == "Sofia":
    if product == "coffee":
        price = 0.50
        print(price * quantity)
    elif product == "water":
        price = 0.80
        price_sum = price * quantity
        print(price * quantity)
    elif product == "beer":
        price = 1.20
        price_sum = price * quantity
        print(price * quantity)
    elif product == "sweets":
        price = 1.45
        price_sum = price * quantity
        print(price * quantity)
    elif product == "peanuts":
        price = 1.60
        price_sum = price * quantity
        print(price * quantity)
elif town == "Plovdiv":
    if product == "coffee":
        price = 0.40
        price_sum = price * quantity
        print(price * quantity)
    elif product == "water":
        price = 0.70
        price_sum = price * quantity
        print(price * quantity)
    elif product == "beer":
        price = 1.15
        price_sum = price * quantity
        print(price * quantity)
    elif product == "sweets":
        price = 1.30
        price_sum = price * quantity
        print(price * quantity)
    elif product == "peanuts":
        price = 1.50
        price_sum = price * quantity
        print(price * quantity)
else:
    if product == "coffee":
        price = 0.45
        price_sum = price * quantity
        print(price * quantity)
    elif product == "water":
        price = 0.70
        price_sum = price * quantity
        print(price * quantity)
    elif product == "beer":
        price = 1.10
        price_sum = price * quantity
        print(price * quantity)
    elif product == "sweets":
        price = 1.35
        price_sum = price * quantity
        print(price * quantity)
    elif product == "peanuts":
        price = 1.55
        price_sum = price * quantity
        print(price * quantity)
