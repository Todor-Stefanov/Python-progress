n = int(input())

unique_chem = set()
for i in range(n):
    chem_comp = list(input().split(" "))
    for g in chem_comp:
        if g not in unique_chem:
            unique_chem.add(g)
for q in unique_chem:
    print(q)
