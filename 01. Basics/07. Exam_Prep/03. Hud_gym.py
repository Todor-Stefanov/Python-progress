country = input()
discipline = input()
max_points = 20

if country == "Russia":
    if discipline == "ribbon":
        difficulty = 9.100
        performance =9.400
        sum_points = difficulty + performance
    elif discipline == "hoop":
        difficulty = 9.300
        performance = 9.800
        sum_points = difficulty + performance
    elif discipline == "rope":
        difficulty = 9.600
        performance = 9.000
        sum_points = difficulty + performance

elif country == "Bulgaria":
    if discipline == "ribbon":
        difficulty = 9.600
        performance = 9.400
        sum_points = difficulty + performance
    elif discipline == "hoop":
        difficulty = 9.550
        performance = 9.750
        sum_points = difficulty + performance
    elif discipline == "rope":
        difficulty = 9.500
        performance = 9.400
        sum_points = difficulty + performance

elif country == "Italy":
    if discipline == "ribbon":
        difficulty = 9.200
        performance = 9.500
        sum_points = difficulty + performance
    elif discipline == "hoop":
        difficulty = 9.450
        performance = 9.350
        sum_points = difficulty + performance
    elif discipline == "rope":
        difficulty = 9.700
        performance = 9.150
        sum_points = difficulty + performance

points_needed = max_points - sum_points
percents_needed = points_needed / max_points * 100

print(f"The team of {country} get {sum_points:.3f} on {discipline}.")
print(f"{percents_needed:.2f}%")


