encrypted_message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    current_command = command[0]
    if current_command == "Move":  # Moves the first n letters to the back of the string
        n = int(command[1])
        encrypted_message = encrypted_message[n:] + encrypted_message[:n]
    elif current_command == "Insert":  # Inserts the given value before the given index in the string
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif current_command == "ChangeAll":  # Changes all occurrences of the given substring with the replacement text
        unwanted_letter = command[1]
        new_letter = command[2]
        while unwanted_letter in encrypted_message:
            encrypted_message = encrypted_message.replace(unwanted_letter, new_letter)

    command = input()

print(f"The decrypted message is: {encrypted_message}")



