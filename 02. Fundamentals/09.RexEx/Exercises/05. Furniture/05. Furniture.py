import re

regex = r">>([A-Za-z]+)<<([0-9]+(\.[0-9]+)*)!([0-9]+)"
furniture = input()
bought_dict = {}
while furniture != "Purchase":
    matches = re.findall(regex, furniture)
    if len(matches) > 0:
        furn, price, space, quantity = matches[0]
        bought_dict[furn] = float(price) * int(quantity)
    furniture = input()

print("Bought furniture:")
total_money = 0
for key, value in bought_dict.items():
    print(key)
    total_money += value
print(f"Total money spend: {total_money:.2f}")
