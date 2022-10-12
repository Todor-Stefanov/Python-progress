number_of_heroes = int(input())
heroes_dict = {}

for i in range(number_of_heroes):
    hero_info = input().split(" ")
    hero_name = hero_info[0]
    hero_hp = int(hero_info[1])
    hero_mp = int(hero_info[2])
    if hero_hp <= 100 and hero_mp <= 200:
        if hero_name not in heroes_dict:
            heroes_dict[hero_name] = {}
            heroes_dict[hero_name]["HP"] = hero_hp
            heroes_dict[hero_name]["MP"] = hero_mp


command = input()
while command != "End":
    command = command.split(" - ")
    current_command = command[0]
    hero_name = command[1]
    if current_command == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes_dict[hero_name]["MP"] >= mp_needed:
            heroes_dict[hero_name]["MP"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif current_command == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes_dict[hero_name]["HP"] -= damage
        if heroes_dict[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")
        else:
            del heroes_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif current_command == "Recharge":
        amount = int(command[2])
        heroes_dict[hero_name]["MP"] += amount
        if heroes_dict[hero_name]["MP"] > 200:
            amount = abs(200 - (heroes_dict[hero_name]["MP"] - amount))
            heroes_dict[hero_name]["MP"] = 200
        print(f"{hero_name} recharged for {amount} MP!")
    elif current_command == "Heal":
        amount = int(command[2])
        heroes_dict[hero_name]["HP"] += amount
        if heroes_dict[hero_name]["HP"] > 100:
            amount = abs(100 - (heroes_dict[hero_name]["HP"] - amount))
            heroes_dict[hero_name]["HP"] = 100
        print(f"{hero_name} healed for {amount} HP!")

    command = input()


for key in heroes_dict.keys():
    print(key)  # Hero name
    print(f"  HP: {heroes_dict[key]['HP']}")
    print(f"  MP: {heroes_dict[key]['MP']}")
