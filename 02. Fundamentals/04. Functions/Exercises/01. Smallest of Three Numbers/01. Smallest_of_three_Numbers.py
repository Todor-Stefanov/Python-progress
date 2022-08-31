def smallest_of(num1: int, num2: int, num3: int):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3


print(smallest_of(num1=int(input()), num2=int(input()), num3=int(input())))


    