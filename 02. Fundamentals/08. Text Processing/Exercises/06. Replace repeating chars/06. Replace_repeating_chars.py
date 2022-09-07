def remove_consec_duplicates(string):
    new_string = ""
    prev = ""
    for ch in string:
        if len(new_string) == 0:
            new_string += ch
            prev = ch
        if ch == prev:
            continue
        else:
            new_string += ch
            prev = ch
    return new_string

string = input()
print(remove_consec_duplicates(string))
