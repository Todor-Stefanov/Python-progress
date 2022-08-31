def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum_result, num3):
    return sum_result - num3


def add_and_subtract(num1, num2, num3):
    print(subtract(sum_numbers(num1, num2), num3))


a = int(input())
b = int(input())
c = int(input())
add_and_subtract(a, b, c)






