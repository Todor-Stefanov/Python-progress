username = input()
password = input()

correct_password = input()
while correct_password != password:
    correct_password = input()

print(f"Welcome {username}!")