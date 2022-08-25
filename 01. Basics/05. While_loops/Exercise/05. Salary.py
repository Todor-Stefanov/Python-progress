num_of_open_tabs = int(input())
salary = int(input())

for _ in range(num_of_open_tabs):
    tab_site = str(input())
    if tab_site == "Facebook" or "Instagram" or "Reddit":
        if tab_site == "Facebook":
            salary -= 150
        elif tab_site == "Instagram":
            salary -= 100
        elif tab_site == "Reddit":
            salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
