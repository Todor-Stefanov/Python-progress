nominee = input()
points = float(input())
judges = int(input())
points_counter = points
for _ in range(judges):
    judge = input()
    points_given = float(input())
    final_points = (len(judge) * points_given) / 2
    points_counter += final_points
    if points_counter >= 1250.5:
        break

points_needed = 1250.50
points_diff = abs(points_counter - points_needed)
if points_counter >= 1250.5:
    print(f"Congratulations, {nominee} got a nominee for leading role with {points_counter:.1f}!")
else:
    print(f"Sorry, {nominee} you need {points_diff:.1f} more!")

