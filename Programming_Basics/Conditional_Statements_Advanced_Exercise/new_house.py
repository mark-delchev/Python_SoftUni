flowers = {
    'Roses': 5,
    'Dahlias': 3.80,
    'Tulips': 2.80,
    'Narcissus': 3,
    'Gladiolus': 2.50
}

flower = str(input())
amount = int(input())
budget = int(input())

price = flowers[flower] * amount

if flower == 'Roses':
    if amount > 80:
        price *= 0.9
    if budget >= price:
        print(f"Hey, you have a great garden with {amount} {flower} and {budget - price:.2f} leva left.")
    elif budget < price:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')

elif flower == 'Dahlias':
    if amount > 90:
        price *= 0.85
    if budget >= price:
        print(f"Hey, you have a great garden with {amount} {flower} and {budget - price:.2f} leva left.")
    elif budget < price:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')

elif flower == 'Tulips':
    if amount > 80:
        price *= 0.85
    if budget >= price:
        print(f"Hey, you have a great garden with {amount} {flower} and {budget - price:.2f} leva left.")
    elif budget < price:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')

elif flower == 'Narcissus':
    if amount < 120:
        price *= 1.15
    if budget >= price:
        print(f"Hey, you have a great garden with {amount} {flower} and {budget - price:.2f} leva left.")
    elif budget < price:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')

elif flower == 'Gladiolus':
    if amount < 80:
        price *= 1.20
    if budget >= price:
        print(f"Hey, you have a great garden with {amount} {flower} and {budget - price:.2f} leva left.")
    elif budget < price:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')