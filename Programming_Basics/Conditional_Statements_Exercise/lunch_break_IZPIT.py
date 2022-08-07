import math

series = str(input())
episode_length = int(input())
break_length = int(input())

lunch_time = break_length * (1/8)
rest_time = break_length * (1/4)
break_length_final = break_length - (lunch_time + rest_time)

if break_length_final >= episode_length:
    print(f'You have enough time to watch {series} and left with {math.ceil (break_length_final-episode_length)} \
minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil (episode_length-break_length_final)} \
more minutes.")

