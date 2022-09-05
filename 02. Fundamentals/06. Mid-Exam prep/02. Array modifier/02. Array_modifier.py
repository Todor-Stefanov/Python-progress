def swap(given_list: list, index1: int, index2: int):
    given_list[index1], given_list[index2] = given_list[index2], given_list[index1]
    return given_list


def multiply(given_list: list, index1: int, index2: int):
    result = given_list[index1] * given_list[index2]
    given_list[index1] = result
    return given_list


array_of_int = list(map(int, input().split(" ")))
command = input().split(" ")

while command[0] != 'end':
    if command[0] == "decrease":
        array_of_int = list(map(lambda x: x - 1, array_of_int))
    else:
        first_index = int(command[1])
        second_index = int(command[2])
        if command[0] == "swap":
            swap(array_of_int, first_index, second_index)
        elif command[0] == "multiply":
            multiply(array_of_int, first_index, second_index)
    command = input().split(" ")

print(*array_of_int, sep=", ")
