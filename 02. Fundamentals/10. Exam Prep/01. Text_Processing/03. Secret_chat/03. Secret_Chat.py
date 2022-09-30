concealed_message = input()

command = input().split(":|:")

while command[0] != "Reveal":
    if command[0] == "InsertSpace":  # Inserts a single space at the given index
        do, index = command
        concealed_message = concealed_message[:int(index)] + " " + concealed_message[int(index):]
        print(concealed_message)
    elif command[0] == "Reverse":  # If the message contains the given substring, cut it out, reverse it and add it
                                   # at the end of the message.
        do, substring = command
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            reversed_substring = substring[::-1]
            concealed_message += reversed_substring
            print(concealed_message)
        else:
            print("error")

    else:  # Changes all occurrences of the given substring with the replacement text
        do, substring, replacement = command
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input().split(":|:")

print(f"You have a new text message: {concealed_message}")