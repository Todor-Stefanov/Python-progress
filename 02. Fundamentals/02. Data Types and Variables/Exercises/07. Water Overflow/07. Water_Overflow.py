capacity = 255
n = int(input())
poured_water = 0
for i in range(n):
    pouring = int(input())

    if poured_water + pouring <= capacity:
        poured_water += pouring
        continue
    print("Insufficient capacity!")
print(poured_water)
