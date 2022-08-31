def change_to_list(string, int_string_list: list):

    for i in range(len(string)):
        string[i] = round(float(string[i]))
        int_string_list.append(string[i])


random_numbers = input().split(" ")
int_string = []
change_to_list(random_numbers, int_string)
print(int_string)
