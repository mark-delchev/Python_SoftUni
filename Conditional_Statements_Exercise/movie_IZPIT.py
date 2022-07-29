budget = float(input())
statists = int(input())
clothing_price = float(input()) * statists
decor = budget * 0.10

if statists > 150:
    clothing_price = clothing_price * 0.90
else:
    clothing_price = clothing_price

expenses = decor + clothing_price
if expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {expenses-budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget-expenses:.2f} leva left.')

