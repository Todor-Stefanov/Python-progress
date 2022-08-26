import math
group_size = int(input())
days = int(input())

companions_count = group_size
coins = 0
spent_coins = 0
for i in range(1, days + 1):

    if i % 10 == 0:
        companions_count -= 2
    if i % 15 == 0:
        companions_count += 5
    coins += 50
    spent_coins = 2 * companions_count

    if i % 3 == 0:
        spent_coins += 3 * companions_count
        # if i % 5 == 0:
        # coins_spent_every_day -= 3 * companions_count
    if i % 5 == 0:
        coins += 20 * companions_count
        if i % 3 == 0:
            spent_coins += 2 * companions_count

    coins -= spent_coins
    coins_spent_every_day = 0

remaining_coins = math.floor(coins / companions_count)
print(f"{companions_count} companions received {remaining_coins} coins each.")
