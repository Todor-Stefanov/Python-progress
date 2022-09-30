raw_activation_key = input()

command = input().split(">>>")
while command[0] != "Generate":
    if command[0] == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":  # Changes the substring between the given indices (the end index is exclusive) to
                                # upper or lower case
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            old_substring = raw_activation_key[start_index:end_index:1]
            new_subsrting = raw_activation_key[start_index:end_index:1].upper()
            raw_activation_key = raw_activation_key.replace(old_substring, new_subsrting)


        else:  # Lower
            old_substring = raw_activation_key[start_index:end_index:1]
            new_subsrting = raw_activation_key[start_index:end_index:1].lower()
            raw_activation_key = raw_activation_key.replace(old_substring, new_subsrting)
        print(raw_activation_key)

    else:
        # Slice - Deletes the characters between the start and end indices (the end index is exclusive)
        start_index = int(command[1])
        end_index = int(command[2])
        old_substring = raw_activation_key[start_index:end_index:1]
        raw_activation_key = raw_activation_key.replace(old_substring, '')
        print(raw_activation_key)


    command = input().split(">>>")

print(f"Your activation key is: {raw_activation_key}")

