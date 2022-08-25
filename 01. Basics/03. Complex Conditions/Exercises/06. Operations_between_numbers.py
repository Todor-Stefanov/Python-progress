n1 = int(input())
n2 = int(input())
operator = input()


if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = n1 + n2
        if n2 == 0:
            print(f"Cannot divide {n1} by zero")
        elif result % 2 == 0:
            print(f"{n1} {operator} {n2} = {result} - even")
        else:
            print(f"{n1} {operator} {n2} = {result} - odd")
    elif operator == "-":
        result = n1 - n2
        if n2 == 0:
            print(f"Cannot divide {n1} by zero")
        elif result % 2 == 0:
            print(f"{n1} {operator} {n2} = {result} - even")
        else:
            print(f"{n1} {operator} {n2} = {result} - odd")
    elif operator == "*":
        result = n1 * n2
        if n2 == 0:
            print(f"Cannot divide {n1} by zero")
        elif result % 2 == 0:
            print(f"{n1} {operator} {n2} = {result} - even")
        else:
            print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {operator} {n2} = {result:.2f}")
if operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {operator} {n2} = {result}")
