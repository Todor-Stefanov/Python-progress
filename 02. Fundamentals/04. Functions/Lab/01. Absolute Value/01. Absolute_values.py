numbers = input().split(" ")
list_str = list(numbers)
list_int = []

for i in range(len(numbers)):
    list_str[i] = abs(float(list_str[i]))
    list_int.append(list_str[i])
print(list_int)
