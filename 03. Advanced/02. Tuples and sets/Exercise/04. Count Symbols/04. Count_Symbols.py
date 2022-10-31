string = tuple(input())

occur = {}
for i in string:
    if i not in occur:
        occur[i] = string.count(i)

sorted_occur = sorted(occur.items())

for key, value in sorted_occur:
    print(f"{key}: {value} time/s")


