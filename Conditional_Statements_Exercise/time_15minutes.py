hour = int(input())
minutes = int(input())

time = hour * 60 + minutes
time15 = time + 15
hours15 = time15 // 60
if hours15 > 23:
    hours15 = 0
minutes15 = time15 % 60
if minutes15 < 10:
    print(f'{hours15}:0{minutes15}')
else:
    print(f'{hours15}:{minutes15}')
