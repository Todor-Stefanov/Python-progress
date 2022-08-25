width = int(input())
lenght = int(input())
cake_pieces = width * lenght
cake_is_over = False
command = input()
while command != "STOP":
    current_number_of_pieces = int(command)
    cake_pieces -= current_number_of_pieces
    if cake_pieces < 0:
        cake_is_over = True
        break

    command = input()
if cake_is_over:  # == True
    print(f"No more cake left! You need {abs(cake_pieces)} peices ")
else:
    print(f"{cake_pieces} pieces left.")