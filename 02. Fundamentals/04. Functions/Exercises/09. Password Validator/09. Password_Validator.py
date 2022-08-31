import string


def pass_validator(password):

    integer_counter = 0
    spec_counter = 0
    for i in password:
        if i in string.digits:
            integer_counter += 1
        if i in string.punctuation:
            spec_counter += 1
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
    if spec_counter > 0:
        print("Password must consist only of letters and digits")
    if integer_counter < 2:
        print("Password must have at least 2 digits")
    if 6 <= len(password) <= 10 and spec_counter == 0 and integer_counter >= 2:
        print("Password is valid")


password = input()
pass_validator(password)
