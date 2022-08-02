prices = [12.00, 7.50, 5.00]
projection_type = str(input())
rows = int(input())
colons = int(input())
seats = rows * colons


if projection_type == 'Premiere':
    price = seats * prices[0]
    print(f'{price:.2f} leva')
elif projection_type == 'Normal':
    price = seats * prices[1]
    print(f'{price:.2f} leva')
elif projection_type == 'Discount':
    price = seats * prices[2]
    print(f'{price:.2f} leva')


