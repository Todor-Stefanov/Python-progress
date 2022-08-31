def overall_price(product, quantity):
    if product == "coffee":
        price = quantity * 1.50
        return f"{price:.2f}"
    elif product == "water":
        price = quantity * 1.00
        return f"{price:.2f}"
    elif product == "coke":
        price = quantity * 1.40
        return f"{price:.2f}"
    elif product == "snacks":
        price = quantity * 2.00
        return f"{price:.2f}"


print(overall_price(product=input(), quantity=int(input())))
