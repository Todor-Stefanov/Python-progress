ord_dict = {}
current_order = input().split(" ")
while current_order[0] != "buy":
    current_product = current_order[0]
    current_price = float(current_order[1])
    current_quantity = int(current_order[2])
    if current_product not in ord_dict:
        ord_dict[current_product] = {}
        ord_dict[current_product]["price"] = current_price
        ord_dict[current_product]["quantity"] = current_quantity
    else:
        if current_price != ord_dict[current_product]["price"]:
            ord_dict[current_product]["price"] = current_price
        ord_dict[current_product]["quantity"] += current_quantity
    current_order = input().split(" ")


for key, value in ord_dict.items():
    print(f"{key} -> {(ord_dict[key]['quantity'] * ord_dict[key]['price']):.2f}")
