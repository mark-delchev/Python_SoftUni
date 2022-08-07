import math

numer_of_tournaments = int(input())
starting_points = int(input())
tournament_points = 0
tournaments_won = 0

for i in range(1, numer_of_tournaments + 1):
    tournament_finish = input()
    if tournament_finish == 'SF':
        tournament_points += 720
    if tournament_finish == 'F':
        tournament_points += 1200
    if tournament_finish == 'W':
        tournament_points += 2000
        tournaments_won += 1

final_points = tournament_points + starting_points
average_points = tournament_points / numer_of_tournaments
average_points_rounded = math.floor(average_points)
win_percentage = (tournaments_won / numer_of_tournaments) * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points_rounded}')
print(f'{win_percentage:.2f}%')



