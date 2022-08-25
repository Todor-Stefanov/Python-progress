number = int(input()) # pokazva kolko chisla mogat da se vyvedat i po tozi nachin kolko chisla da se suberat

total_sum = 0
for _ in range(number):
    current_num = int(input())
    total_sum += current_num

print(total_sum)
