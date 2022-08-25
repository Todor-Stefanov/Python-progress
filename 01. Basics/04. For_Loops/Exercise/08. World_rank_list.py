import math
tournament_number = int(input())
starting_points = int(input())

points_counter = starting_points
winned_tournaments_counter = 0
for _ in range(tournament_number):
    reached_level = input()
    if reached_level == "W":
        points_counter += 2000
        winned_tournaments_counter += 1
    elif reached_level == "F":
        points_counter += 1200
    elif reached_level == "SF":
        points_counter += 720

average_points_per_tournament = (points_counter - starting_points) / tournament_number
percent_won_tournaments = (winned_tournaments_counter / tournament_number) * 100
print(f"Final points: {points_counter}")
print(f"Average points: {math.floor(average_points_per_tournament)}")
print(f"{percent_won_tournaments:.2f}%")

