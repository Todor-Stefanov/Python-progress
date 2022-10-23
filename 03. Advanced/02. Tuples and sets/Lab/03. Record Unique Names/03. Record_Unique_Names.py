number_of_names = int(input())

list_of_names = []
for i in range(number_of_names):
    name = input()
    list_of_names.append(name)
unique = {name for name in list_of_names}

for i in unique:
    print(i)