lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

repair_cost = 0
broken_shield_counter = 0
for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        repair_cost += helmet_price
    if i % 3 == 0:
        repair_cost += sword_price
        if i % 2 == 0:
            broken_shield_counter += 1
            repair_cost += shield_price
            if broken_shield_counter % 2 == 0:
                repair_cost += armor_price

print(f"Gladiator expenses: {repair_cost:.2f} aureus")
