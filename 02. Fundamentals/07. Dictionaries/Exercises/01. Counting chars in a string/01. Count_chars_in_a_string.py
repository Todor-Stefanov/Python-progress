my_dict = {}
word = input()

for i in word:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for ch in my_dict.keys():
    if ch != " ":
        print(f"{ch} -> {my_dict[ch]}")



# from collection import Counter
#word = input()
#result = Counter(word)

#for key, value in result.items():
#   if key != ' ':
#        print(f'{key} -> {value}')
