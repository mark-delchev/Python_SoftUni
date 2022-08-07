actor_name = input()
academy_points = float(input())
number_of_judges = int(input())
judge_points_final = 0

for i in range(1, number_of_judges + 1):
    judge_name = input()
    judge_points = float(input())
    name_length = len(judge_name)
    judge_points_final += (judge_points * name_length) / 2
    if judge_points_final + academy_points > 1250.5:
        break

final_points = judge_points_final + academy_points

if judge_points_final + academy_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!')
elif judge_points_final + academy_points <= 1250.5:
    print(f'Sorry, {actor_name} you need {1250.5 - final_points:.1f} more!')
