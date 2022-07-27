work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
price_work_days = {
    'banana': 2.50,
    'apple': 1.20,
    'orange': 0.85,
    'grapefruit': 1.45,
    'kiwi': 2.70,
    'pineapple': 5.50,
    'grapes': 3.85
}

price_weekend = {
    'banana': 2.70,
    'apple': 1.25,
    'orange': 0.90,
    'grapefruit': 1.60,
    'kiwi': 3.00,
    'pineapple': 5.60,
    'grapes': 4.20
}

fruit = str(input())
day = str(input())
amount = float(input())

if day in work_days:
    if fruit in price_work_days:
        price = price_work_days[fruit] * amount
        print(f'{price:.2f}')
    else:
        print('error')
elif day in weekend:
    if fruit in price_weekend:
        price = price_weekend[fruit] * amount
        print(f'{price:.2f}')
    else:
        print('error')
else:
    print('error')