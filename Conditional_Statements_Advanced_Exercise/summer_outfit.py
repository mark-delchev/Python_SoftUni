degrees = int(input())
time = str(input())
outfit = ['Sweatshirt', 'Shirt', 'T-Shirt', 'Swim Suit']
shoes = ['Sneakers', 'Moccasins', 'Sandals', 'Barefoot']

if time == 'Morning':
    if 10 <= degrees <= 18:
        print(f"It's {degrees} degrees, get your {outfit[0]} and {shoes[0]}.")
    elif 18 < degrees <= 24:
        print(f"It's {degrees} degrees, get your {outfit[1]} and {shoes[1]}.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your {outfit[2]} and {shoes[2]}.")

elif time == 'Afternoon':
    if 10 <= degrees <= 18:
        print(f"It's {degrees} degrees, get your {outfit[1]} and {shoes[1]}.")
    elif 18 < degrees <= 24:
        print(f"It's {degrees} degrees, get your {outfit[2]} and {shoes[2]}.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your {outfit[3]} and {shoes[3]}.")

elif time == 'Evening':
    if 10 <= degrees <= 18:
        print(f"It's {degrees} degrees, get your {outfit[1]} and {shoes[1]}.")
    elif 18 < degrees <= 24:
        print(f"It's {degrees} degrees, get your {outfit[1]} and {shoes[1]}.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your {outfit[1]} and {shoes[1]}.")