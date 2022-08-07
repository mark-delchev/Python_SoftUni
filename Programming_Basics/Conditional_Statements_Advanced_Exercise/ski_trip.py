days = int(input())
type_of_room = str(input())
grade = str(input())
prices = {
    "room for one person": 18.00,
    "apartment": 25.00,
    "president apartment": 35.00
}
if type_of_room == "room for one person":
    price = prices[type_of_room] * (days - 1)
    if grade == "negative":
        price *= 0.90
        print(f'{price:.2f}')
    elif grade == "positive":
        price *= 1.25
        print(f'{price:.2f}')
elif type_of_room == "apartment":
    price = prices[type_of_room] * (days - 1)
    if days < 10:
        price *= 0.70
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.50
    if grade == "negative":
        price *= 0.90
        print(f'{price:.2f}')
    elif grade == "positive":
        price *= 1.25
        print(f'{price:.2f}')
elif type_of_room == "president apartment":
    price = prices[type_of_room] * (days - 1)
    if days < 10:
        price *= 0.90
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.80
    if grade == "negative":
        price *= 0.90
        print(f'{price:.2f}')
    elif grade == "positive":
        price *= 1.25
        print(f'{price:.2f}')



