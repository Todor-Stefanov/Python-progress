def taxes(price_of_current_product):
    tax = 0.2 * price_of_current_product
    return tax


def receipt(total_price_without_taxes, total_amount_of_taxes, total_price_with_taxes):

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")


command = input()

total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0
customer = ""
while command != "special" or command != "regular":
    if command == "special" or command == "regular":
        customer = command
        break
    float_command = float(command)
    if float_command < 0:
        print("Invalid price!")
        float_command = 0
    total_price_without_taxes += float_command
    total_amount_of_taxes += taxes(float_command)
    total_price_with_taxes += float_command + taxes(float_command)
    command = input()

if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    if customer == "special":
        total_price_with_taxes = total_price_with_taxes - 0.1 * total_price_with_taxes
    receipt(total_price_without_taxes, total_amount_of_taxes, total_price_with_taxes)
