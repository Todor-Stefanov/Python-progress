town = input()
sell_volume = float(input())

if sell_volume < 0:
    print("error")
elif town == "Sofia":
    if 0 <= sell_volume <= 500:
        commicion = sell_volume * 5 / 100
        print(f'{commicion:.2f}')
    elif 500 < sell_volume <= 1000:
        commicion = sell_volume * 7 / 100
        print(f'{commicion:.2f}')
    elif 1000 < sell_volume <= 10000:
        commicion = sell_volume * 8 / 100
        print(f'{commicion:.2f}')
    elif sell_volume > 10000:
        commicion = sell_volume * 12 / 100
        print(f'{commicion:.2f}')
elif town == "Varna":
    if 0 <= sell_volume <= 500:
        commicion = sell_volume * 4.5 / 100
        print(f'{commicion:.2f}')
    elif 500 < sell_volume <= 1000:
        commicion = sell_volume * 7.5 / 100
        print(f'{commicion:.2f}')
    elif 1000 < sell_volume <= 10000:
        commicion = sell_volume * 10 / 100
        print(f'{commicion:.2f}')
    elif sell_volume > 10000:
        commicion = sell_volume * 13 / 100
        print(f'{commicion:.2f}')
elif town == "Plovdiv":
    if 0 <= sell_volume <= 500:
        commicion = sell_volume * 5.5 / 100
        print(f'{commicion:.2f}')
    elif 500 < sell_volume <= 1000:
        commicion = sell_volume * 8 / 100
        print(f'{commicion:.2f}')
    elif 1000 < sell_volume <= 10000:
        commicion = sell_volume * 12 / 100
        print(f'{commicion:.2f}')
    elif sell_volume > 10000:
        commicion = sell_volume * 14.5 / 100
        print(f'{commicion:.2f}')
else:
    if town != "Sofia" or town != "Varna" or town != "Plovdiv":
        print("error")
