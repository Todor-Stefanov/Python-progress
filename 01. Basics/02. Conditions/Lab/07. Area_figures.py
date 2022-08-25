import math

figure = input()

if figure == 'square':
    num = float(input())
    result = num * num
    print(f'{result:.3f}')

elif figure == 'rectangle':
    num1 = float(input())
    num2 = float(input())
    result = num1 * num2
    print(f'{result:.3f}')

elif figure == 'circle':
    num = float(input())
    result = math.pi * (num ** 2)
    print(f'{result:.3f}')

elif figure == 'triangle':
    num1 = float(input())
    num2 = float(input())
    result = num1 * num2 / 2
    print(f'{result:.3f}')
