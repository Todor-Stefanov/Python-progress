num = int(input())
word = input()

whole_list = []
key_word_list = []

for n in range(num):
    current_sentence = input()
    whole_list.append(current_sentence)
    if word in current_sentence:
        key_word_list.append(current_sentence)
print(whole_list)
print(key_word_list)
