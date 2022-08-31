def find_ascii_between(a, b):
    string = list()
    for i in range(ord(a) + 1, ord(b)):
        char = chr(i)
        string.append(char)
    return string


def from_list_to_string(list_to_str):
    print(" ".join(map(str, list_to_str)))


first_char = input()
second_char = input()
from_list_to_string((find_ascii_between(first_char, second_char)))
