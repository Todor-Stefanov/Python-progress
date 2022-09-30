
import re

text = input()
regex = r"\#([A-Za-z\s]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|\|([A-Za-z\s]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|"

matches = re.findall(regex, text)

sum_cals = 0
output_list = []
if len(matches) > 0:
    for i in range(len(matches)):
        if matches[i][0] != "":
            food = matches[i][0]
            date = matches[i][1]
            calories = matches[i][2]
            sum_cals += int(calories)
            output_list.append(f"Item: {food}, Best before: {date}, Nutrition: {calories}")
        else:
            food = matches[i][3]
            date = matches[i][4]
            calories = matches[i][5]
            sum_cals += int(calories)
            output_list.append(f"Item: {food}, Best before: {date}, Nutrition: {calories}")


print(f"You have food to last you for: {int(sum_cals/2000)} days!")
if len(output_list) > 0:
    for match in output_list:
        print(match)
