budget = float(input())
season = input()

destination = ''
sleep = ''
price_per_stay = 0
if season == "summer":
    if budget <= 100:
        destination = 'Bulgaria'
        sleep = "Camp"
        price_per_stay = budget * 30 / 100

    elif 100 < budget <= 1000:
        destination = "Balkans"
        sleep = "Camp"
        price_per_stay = budget * 40 / 100
    else:
        destination = "Europe"
        sleep = "Hotel"
        price_per_stay = budget * 90 / 100

elif season == "winter":
    if budget <= 100:
        destination = 'Bulgaria'
        sleep = "Hotel"
        price_per_stay = budget * 70 / 100

    elif 100 < budget <= 1000:
        destination = "Balkans"
        sleep = "Hotel"
        price_per_stay = budget * 80 / 100
    else:
        destination = "Europe"
        sleep = "Hotel"
        price_per_stay = budget * 90 / 100
print(f"Somewhere in {destination}")
print(f"{sleep} - {price_per_stay:.2f}")

