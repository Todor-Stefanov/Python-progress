number = int(input())

sum_left = 0
sum_right = 0

for _ in range(number):
    current_number = int(input())
    sum_left += current_number
for _ in range(number):
    current_number = int(input())
    sum_right += current_number

sum_sum = sum_left
sum_dif = abs(sum_right - sum_left)

if sum_left - sum_right == 0:
    print(f"Yes, sum = {sum_sum}")
else:
    print(f"No, diff = {sum_dif}")
