words = input().split(" ")
palindrom_words = list()
palindrome = input()

for word in words:
    rev_list = reversed(word)
    rev_word = "".join(rev_list)

    if rev_word == word:
        palindrom_words.append(word)

print(palindrom_words)
palindrome_count = words.count(palindrome)
print(f"Found palindrome {palindrome_count} times")