month = input()
nights = int(input())

price_ap = 0
price_studio = 0
room_ap = "Apartment"
room_studio = "Studio"

if room_ap and nights > 14:
    if month == "May" or month == "October":
        price_ap = 65 - (65 * 10 / 100)
    elif month == "June" or month == "September":
        price_ap = 68.70 - (68.70 * 10 / 100)
    elif month == "July" or month == "August":
        price_ap = 77 - (77 * 10 / 100)
elif room_ap and nights <= 14:
    if month == "May" or month == "October":
        price_ap = 65
    elif month == "June" or month == "September":
        price_ap = 68.70
    elif month == "July" or month == "August":
        price_ap = 77

if room_studio and (month == "May" or month == "October"):
    if 7 < nights <= 14:
        price_studio = 50 - (50 * 5 / 100)
    elif nights > 14:
        price_studio = 50 - (50 * 30 / 100)
    elif nights <= 7:
        price_studio = 50
elif room_studio and (month == "June" or month == "September"):
    if nights > 14:
        price_studio = 75.20 - (75.20 * 20 / 100)
    elif nights <= 14:
        price_studio = 75.20
elif room_studio and (month == "July" or month == "August"):
    price_studio = 76

overall_price_ap = price_ap * nights
overall_price_studio = price_studio * nights

print(f"{room_ap}: {overall_price_ap:.2f} lv.")
print(f"{room_studio}: {overall_price_studio:.2f} lv.")
