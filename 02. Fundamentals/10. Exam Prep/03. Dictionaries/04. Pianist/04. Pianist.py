n = int(input())

pieces_dict = {}
for i in range(n):
    pieces_input = input().split("|")
    piece, composer, key = pieces_input
    if piece not in pieces_dict:
        pieces_dict[piece] = {}
        pieces_dict[piece]["composer"] = composer
        pieces_dict[piece]["key"] = key

command = input().split("|")

while command[0] != "Stop":
    if command[0] == "Add":
        do, piece, composer, key = command
        if piece not in pieces_dict.keys():
            pieces_dict[piece] = {}
            pieces_dict[piece]["composer"] = composer
            pieces_dict[piece]["key"] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        do, piece = command
        if piece in pieces_dict.keys():
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        do, piece, new_key = command
        if piece in pieces_dict:
            pieces_dict[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input().split("|")

for key, value in pieces_dict.items():
    current_items = []
    current_items.append(key)
    for nested_key, nested_value in value.items():
        current_items.append(nested_value)

    print(f"{current_items[0]} -> Composer: {current_items[1]}, Key: {current_items[2]}")