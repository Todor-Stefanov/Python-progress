number_of_usernames = int(input())

unique_usernames = set()
for i in range(number_of_usernames):
    username = input()
    if username not in unique_usernames:
        unique_usernames.add(username)

for name in unique_usernames:
    print(name)
