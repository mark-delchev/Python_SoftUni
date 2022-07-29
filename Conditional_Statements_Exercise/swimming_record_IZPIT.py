import math

record = float(input())
distance = float(input())
speed = float(input())
times_slowed_down = distance / 15
slow_down = math.floor(times_slowed_down)
seconds_lost = slow_down * 12.5

time = distance * speed + seconds_lost
if time < record:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    print(f'No, he failed! He was {time-record:.2f} seconds slower.')

