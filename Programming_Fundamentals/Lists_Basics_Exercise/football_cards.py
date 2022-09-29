team_A = list(i for i in range(1, 12))
team_B = list(i for i in range(1, 12))

team = []
player = []

info = input()
info_split = info.split(sep=" ")
info_split_str = "-".join(info_split)
team_player = info_split_str.split(sep="-")
for i in range(len(team_player)):
    if i % 2 == 0:
        team.append(team_player[i])
    else:
        player.append(team_player[i])

for i in range(len(team)):
    if len(team_A) < 7 or len(team_B) < 7:
        break
    try:
        if team[i] == "A":
            team_A.remove(int(player[i]))
        else:
            team_B.remove(int(player[i]))
    except ValueError:
        continue

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if len(team_A) < 7 or len(team_B) < 7:
    print("Game was terminated")