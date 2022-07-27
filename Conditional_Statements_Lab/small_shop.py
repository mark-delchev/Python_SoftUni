S_coffee = 0.50
P_coffee = 0.40
V_coffee = 0.45

S_water = 0.80
P_water = 0.70
V_water = 0.70

S_beer = 1.20
P_beer = 1.15
V_beer = 1.10

S_sweets = 1.45
P_sweets = 1.30
V_sweets = 1.35

S_peanuts = 1.60
P_peanuts = 1.50
V_peanuts = 1.55

product = str(input())
city = str(input())
amount = float(input())

if product == 'coffee':
    if city == 'Sofia':
        print(S_coffee * amount)
    elif city == 'Plovdiv':
        print(P_coffee * amount)
    elif city == 'Varna':
        print(V_coffee * amount)

elif product == 'water':
    if city == 'Sofia':
        print(S_water * amount)
    elif city == 'Plovdiv':
        print(P_water * amount)
    elif city == 'Varna':
        print(V_water * amount)

elif product == 'beer':
    if city == 'Sofia':
        print(S_beer * amount)
    elif city == 'Plovdiv':
        print(P_beer * amount)
    elif city == 'Varna':
        print(V_beer * amount)

elif product == 'sweets':
    if city == 'Sofia':
        print(S_sweets * amount)
    elif city == 'Plovdiv':
        print(P_sweets * amount)
    elif city == 'Varna':
        print(V_sweets * amount)

elif product == 'peanuts':
    if city == 'Sofia':
        print(S_peanuts * amount)
    elif city == 'Plovdiv':
        print(P_peanuts * amount)
    elif city == 'Varna':
        print(V_peanuts * amount)