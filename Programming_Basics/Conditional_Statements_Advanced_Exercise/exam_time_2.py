hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())
time_of_exam = hour_of_exam * 60 + minutes_of_exam
time_of_arrival = hour_of_arrival * 60 + minutes_of_arrival
time = abs(time_of_exam - time_of_arrival)
hours = time // 60
minutes = time % 60

if time_of_arrival == time_of_exam:
    print('On time')
elif time_of_exam > time_of_arrival >= time_of_exam - 30:
    print('On time')
    print(f'{minutes} minutes before the start')
elif time_of_arrival >= time_of_exam + 60:
    print('Late')
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")
elif time_of_exam + 60 > time_of_arrival > time_of_exam:
    print('Late')
    print(f"{minutes} minutes after the start")
elif time_of_exam - 60 < time_of_arrival < time_of_exam - 30:
    print('Early')
    print(f'{minutes} minutes before the start')
elif time_of_exam - 60 >= time_of_arrival:
    print('Early')
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")




