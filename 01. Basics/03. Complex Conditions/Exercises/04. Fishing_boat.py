budget = int(input())
season = input()
number_of_fishermen = int(input())
boat_rent = 0 #promenliva

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn": #pravilen sintaksis
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600
#--------------------------------------------------
if number_of_fishermen <= 6:
    boat_rent *= 0.9   #boat_rent = boat_rent - (boat_rent * 0.9)
elif number_of_fishermen <= 11:
    boat_rent *= 0.85
else:   # if_number_of_fishermen >= 12
    boat_rent *= 0.75

if season != "Autumn" and number_of_fishermen % 2 == 0: # not season == "Autumn"
    boat_rent *= 0.95

difference = abs(budget - boat_rent) # abs dava polovitelnata stoinost
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
    