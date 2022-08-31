# parameter_input = input()
# number1 = int(input())
# number2 = int(input())


def calculator(num1, num2, parameter):
    if parameter == "multiply":
        multiple = num1 * num2
        return multiple
    elif parameter == "divide":
        division = int(num1 / num2)
        return division
    elif parameter == "subtract":
        subtraction = num1 - num2
        return subtraction
    elif parameter == "add":
        addition = num1 + num2
        return addition


print(calculator(parameter=input(), num1=int(input()), num2=int(input())))
