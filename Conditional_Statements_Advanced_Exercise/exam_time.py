hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

if hour_of_exam == hour_of_arrival and minutes_of_exam == minutes_of_arrival:
    print('On time')
elif hour_of_exam == hour_of_arrival and minutes_of_exam != minutes_of_arrival:
    if minutes_of_exam - minutes_of_arrival < 0:
        print('Late')
        print(f'{minutes_of_arrival - minutes_of_exam} minutes after the start')
    if 0 < minutes_of_exam - minutes_of_arrival <= 30:
        print('On time')
        print(f'{minutes_of_exam - minutes_of_arrival} minutes before the start')
    if minutes_of_exam - minutes_of_arrival > 30:
        print('Early')
        print(f'{minutes_of_exam - minutes_of_arrival} minutes before the start')
elif hour_of_exam > hour_of_arrival and minutes_of_exam == minutes_of_arrival:
    print('Early')
    print(f'{hour_of_exam - hour_of_arrival}:00 hours before the start')
elif hour_of_exam > hour_of_arrival and minutes_of_exam != minutes_of_arrival:
    if hour_of_exam - hour_of_arrival == 1 and 60 + minutes_of_exam - minutes_of_arrival > 30:
        print('Early')
        if -1 < minutes_of_exam - minutes_of_arrival < 10:
            print(f'{hour_of_exam - hour_of_arrival}:0{minutes_of_exam - minutes_of_arrival} hours before the start')
        elif 60 + minutes_of_exam - minutes_of_arrival > 59:
            print(f'{hour_of_exam - hour_of_arrival}:{minutes_of_exam - minutes_of_arrival} hours before the start')
        else:
            print(f'{(60 + minutes_of_exam - minutes_of_arrival)} minutes before the start')
    elif hour_of_exam - hour_of_arrival > 1 and minutes_of_exam != minutes_of_arrival:
        print('Early')
        if 60 + minutes_of_exam - minutes_of_arrival < 10:
            print(f'{hour_of_exam - hour_of_arrival - 1}:0{(60 + minutes_of_exam - minutes_of_arrival)} hours before the start')
        elif minutes_of_exam < minutes_of_arrival:
            print(f'{hour_of_exam - hour_of_arrival}:{-(minutes_of_exam - minutes_of_arrival)} hours before the start')
        else:
            print(f'{hour_of_exam - hour_of_arrival}:{(minutes_of_exam - minutes_of_arrival)} hours before the start')
    elif hour_of_exam - hour_of_arrival == 1 and 60 + minutes_of_exam - minutes_of_arrival <= 30:
        print('On time')
        print(f'{60 -(-(minutes_of_exam - minutes_of_arrival))} minutes before the start')
elif hour_of_exam < hour_of_arrival and minutes_of_exam == minutes_of_arrival:
    print('Late')
    print(f'{hour_of_arrival - hour_of_exam}:00 hours after the start')
elif hour_of_exam < hour_of_arrival and minutes_of_exam != minutes_of_arrival:
    print('Late')
    if hour_of_arrival - hour_of_exam == 1 and minutes_of_arrival < minutes_of_exam:
        print(f'{60-(minutes_of_exam - minutes_of_arrival)} minutes after the start')
    elif minutes_of_arrival < 10:
        print(f'{hour_of_arrival - hour_of_exam}:0{-(minutes_of_exam - minutes_of_arrival)} hours after the start')
    else:
        print(f'{hour_of_arrival - hour_of_exam}:{-(minutes_of_exam - minutes_of_arrival)} hours after the start')




