n_m = list(map(int, input().split(" ")))

n_set = set()
m_set = set()

counter = 1
for i in range(n_m[0] + n_m[1]):
    number = input()
    if counter <= n_m[0]:
        n_set.add(number)
    else:
        m_set.add(number)

    counter += 1

intercept = n_set & m_set
for g in intercept:
    print(g)
