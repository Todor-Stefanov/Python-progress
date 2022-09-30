all_stops = input()

command = input()
while command != "Travel":
    command = command.split(":")
    current_command = command[0]
    if current_command == 'Add Stop':  # Insert the given string at that index only if the index is valid
        all_stops_list = list(map(str, all_stops))
        index = int(command[1])
        new_stop = command[2]
        if index >= 0 and index < len(all_stops_list):
           all_stops_list.insert(index, new_stop)
           all_stops = ""
           for ch in all_stops_list:
               all_stops += ch

    elif current_command == "Remove Stop":  # Remove the elements of the string from the starting index to the end
                                            # index (inclusive) if both indices are valid
        starting_index = int(command[1])
        end_index = int(command[2])
        if 0 <= starting_index < len(all_stops) and end_index >= 0 and end_index < len(all_stops):
            all_stops = all_stops[0 : starting_index :] + all_stops[end_index + 1 ::]
    elif current_command == "Switch": # If the old string is in the initial string, replace it with the new one (all occurrences)
        old_string = command[1]
        new_string = command[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
    print(all_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {all_stops}")

