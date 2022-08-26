first_char = int(input())
last_char = int(input())

a = ""
for i in range(first_char, last_char + 1):
    a = chr(i)
    print(a, end=" ")
