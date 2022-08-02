season_rent = {
    'Spring': 3000,
    'Summer': 4200,
    'Autumn': 4200,
    'Winter': 2600
}
budget = int(input())
season = input()
fishermen = int(input())

price = season_rent[season]
if season != 'Autumn' and fishermen % 2 == 0:
    price *= 0.95


if fishermen <= 6:
    price *= 0.90
    if budget >= price:
        print(f'Yes! You have {budget - price:.2f} leva left.')
    elif price > budget:
        print(f'Not enough money! You need {price - budget:.2f} leva.')
elif 7 <= fishermen <= 11:
    price *= 0.85
    if budget >= price:
        print(f'Yes! You have {budget - price:.2f} leva left.')
    elif price > budget:
        print(f'Not enough money! You need {price - budget:.2f} leva.')
elif fishermen > 12:
    price *= 0.75
    if budget >= price:
        print(f'Yes! You have {budget - price:.2f} leva left.')
    elif price > budget:
        print(f'Not enough money! You need {price - budget:.2f} leva.')

