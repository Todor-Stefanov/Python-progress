days = int(input())
room_type = input()
feedback = input()

room_for_one = 18.00
apartment = 25.00
president_apartment = 35.00
nights = days - 1
price = 0
if room_type == "room for one person":
    price = 18
elif room_type == "apartment":
    if days < 10:
        price = 25 - (25 * 30 / 100)
    elif 10 <= days <= 15:
        price = 25 - (25 * 35 / 100)
    elif days > 15:
        price = 25 - (25 / 2)
elif room_type == "president apartment":
    if days < 10:
        price = 35 - (35 * 10 / 100)
    elif 10 <= days <= 15:
        price = 35 - (35 * 15 / 100)
    elif days > 15:
        price = 35 - (35 * 20 / 100)
overall_price = nights * price

if feedback == "positive":
    discount = overall_price + (overall_price * 25 / 100)
    print(f"{discount:.2f}")
elif feedback == "negative":
    discount = overall_price - (overall_price * 10 / 100)
    print(f"{discount:.2f}")

