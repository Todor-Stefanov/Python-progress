budget = float(input())
N = int(input())
M = int(input())
P = int(input())

N_price = 250 * N
M_price = 35 / 100 * N_price * M
P_price = 10 / 100 * N_price * P

overall = N_price + M_price + P_price
if N > M:
    overall = overall - (15 / 100 * overall)

if budget >= overall:
    print(f'You have {(budget - overall):.2f} leva left!')
else:
    print(f'Not enough money! You need {(overall - budget):.2f} leva more!')

