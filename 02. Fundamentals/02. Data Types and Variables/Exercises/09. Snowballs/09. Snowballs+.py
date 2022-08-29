N = int(input())

best_snowball = 0
best_list = [0, 1, 2, 3]
for i in range(N):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_snowball_value = int((weight / time_needed)) ** quality
    current_list = [weight, time_needed, current_snowball_value, quality]
    if current_snowball_value > best_snowball:
        best_snowball = current_snowball_value
        best_list = current_list
        continue


print(f'{best_list[0]} : {best_list[1]} = {best_list[2]} ({best_list[3]})')