num = int(input())
for n in range(1, num+1):
    current_number = n
    digit_sum = 0
    while current_number > 0:
        digit_sum += current_number % 10
        current_number = int(current_number / 10)

    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum ==11
    print(f"{n} -> {is_special}")