lenght = int(input())
width = int(input())
height = int(input())

percents = float(input())
vol = lenght * width * height
vol_liters = vol * 0.001
space = percents / 100
liters_needed = vol_liters * (1 - space)
print(liters_needed)
