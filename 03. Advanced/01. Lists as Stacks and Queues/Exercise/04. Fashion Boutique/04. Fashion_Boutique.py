clothes_in_the_box = input().split(" ")  # 5 4 8 6 3 8 7 7 9
capacity_of_a_rack = int(input())  # 16

stack = list(clothes_in_the_box)  # ['5', '4', '8', '6', '3', '8', '7', '7', '9']

sum_clothes = 0
racks_counter = 0
while len(stack) != 0:
    current_cloth = int(stack.pop())
    sum_clothes += current_cloth
    if sum_clothes == capacity_of_a_rack:
        racks_counter += 1
        if len(stack) >= 0:
            sum_clothes = 0
    if sum_clothes > capacity_of_a_rack:
        sum_clothes = 0
        racks_counter += 1
        stack.append(current_cloth)
if sum_clothes > 0:
    racks_counter += 1

print(racks_counter)