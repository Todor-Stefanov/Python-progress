search = input()
text = input()

while search in text: # Докато стринга на search се намира в text
    text = text.replace(search, "")

print(text)
