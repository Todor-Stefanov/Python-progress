string = input().split(" ")
shuffles = int(input())

new_list = list(string)
for i in range(shuffles):
    A = new_list[:len(new_list) // 2]
    B = new_list[len(new_list) // 2:]
    new_list = [c for pair in zip(A, B) for c in pair]

print(new_list)


