needed_money = float(input())
money_in_hand = float(input())

saved_money = money_in_hand
day_counter = 0
spending_counter = 0
while saved_money != needed_money and spending_counter < 5:
    action = input()
    sum_per_action = float(input())
    day_counter += 1
    if action == "save":
        saved_money += sum_per_action
        if spending_counter > 0:
            spending_counter = 0
    elif action == "spend":
        saved_money -= sum_per_action
        spending_counter += 1
        if saved_money < 0:
            saved_money = 0

if saved_money >= needed_money:
    print(f"You saved the money for {day_counter} days.")
if spending_counter == 5:
    print("You can't save the money.")
    print(f"{day_counter}")

