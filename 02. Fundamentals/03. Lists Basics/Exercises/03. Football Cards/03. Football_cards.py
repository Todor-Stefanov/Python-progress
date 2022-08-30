removed_players = input().split(" ")

teamA_list = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
teamB_list = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

for player_number in removed_players:
    if player_number in teamA_list:
        teamA_list.remove(player_number)
    elif player_number in teamB_list:
        teamB_list.remove(player_number)
    if len(teamA_list) < 7 or len(teamB_list) < 7:
        break
    else:
        continue

print(f"Team A - {len(teamA_list)}; Team B - {len(teamB_list)}")

if len(teamA_list) < 7 or len(teamB_list) < 7:
    print("Game was terminated")

