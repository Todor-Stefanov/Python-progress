vowels = ["a", "o", "u", "e", "i"]
text_string = list(map(str, input()))
remove_vowels = [letter for letter in text_string if letter not in vowels]
print(*remove_vowels, sep="")