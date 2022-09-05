def phonebook_information(number_of_lines, phone_book):
    for x in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")

    return True


def phonebook():
    phone_book = {}
    condition = False

    while True:
        contact_info = input().split("-")

        if contact_info[0].isdigit():
            condition = phonebook_information(int(contact_info[0]), phone_book)
        else:
            phone_book[contact_info[0]] = contact_info[1]

        if condition:
            break



phonebook()

