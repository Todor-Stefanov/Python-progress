names = input().split(", ")
sorted_names = sorted(names, key=lambda x: (-len(x), x)) #-len(x) по дължина, х - по азбучен ред
print(sorted_names)
