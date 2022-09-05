product = input().split(": ")
product_dict = {}
total_products = 0
total_quantity = 0

while product[0] != "statistics":
    key = product[0]
    value = product[1]
    if product[0] in product_dict.keys():
        product_dict[product[0]] += int(value)
    else:
        product_dict[key] = int(value)
    product = input().split(": ")

print("Products in stock:")
for key in product_dict.keys():
    total_products += 1
    total_quantity += product_dict[key]
    print(f"- {key}: {product_dict[key]}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")

