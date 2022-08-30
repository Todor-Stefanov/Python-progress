int_string = input().split(" ")
remove_num = int(input())

str_list = list(int_string)
int_list = []
for i in range(len(str_list)):
    str_list[i] = int(str_list[i])
    int_list.append(str_list[i])

for i in range(remove_num):
    int_list.remove(min(int_list))

print(', '.join(map(str, int_list)))

