budget = float(input())
season = input()

if season == 'summer':
    if budget > 1000:
        type_of_accommodation = 'Hotel'
    else:
        type_of_accommodation = 'Camp'
elif season == 'winter':
    type_of_accommodation = 'Hotel'

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expenses = budget * 0.30
    elif season == 'winter':
        expenses = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expenses = budget * 0.40
    elif season == 'winter':
        expenses = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer':
        expenses = budget * 0.90
    elif season == 'winter':
        expenses = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{type_of_accommodation} - {expenses:.2f}')

