money = input().split(", ")
beggars = int(input())

money_list = list(money)
current_sum = 0
modified_list = []
beggars_list = []
for i in range(len(money_list)):
    money_list[i] = int(money_list[i])
    modified_list.append(money_list[i])

for beggar in range(beggars):
    current_sum = sum(modified_list[beggar::beggars]) #sumiram ot ntiq element prez n elementa 
    beggars_list.append(current_sum)

print(beggars_list)



