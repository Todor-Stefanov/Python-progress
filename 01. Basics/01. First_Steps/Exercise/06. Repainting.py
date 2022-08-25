nailon = int(input()) * 1.50
boq = int(input()) * 14.50
razreditel = int(input()) * 5.00
hours = int(input())

bonus_boq = boq + (10 / 100 * boq)
bonus_naion = nailon + (2 * 1.50)
bags = 0.40

sum_materials = bonus_naion + bonus_boq + razreditel + bags
sum_worker = (sum_materials * 30 / 100) * hours

final_sum = sum_materials + sum_worker

print(final_sum)

