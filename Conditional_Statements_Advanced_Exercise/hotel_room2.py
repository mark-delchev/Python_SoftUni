month = str(input())
days = float(input())

Studio_may = 50
Apartment_may = 65
Studio_june = 75.20
Apartment_june = 68.70
Studio_july = 76
Apartment_july = 77

if days > 14:
    Apartment_may *= 0.9
    Apartment_june *= 0.9
    Apartment_july *= 0.9
if month == 'May' or month == 'October':
    if 14 >= days > 7:
        Studio_may *= 0.95
    elif days > 14:
        Studio_may *= 0.70
    print(f"Apartment: {Apartment_may * days:.2f} lv.")
    print(f"Studio: {Studio_may * days:.2f} lv.")
elif month == 'June' or month == 'September':
    if days > 14:
        Studio_june *= 0.80
    print(f"Apartment: {Apartment_june * days:.2f} lv.")
    print(f"Studio: {Studio_june * days:.2f} lv.")
elif month == 'July' or month == 'August':
    print(f"Apartment: {Apartment_july * days:.2f} lv.")
    print(f"Studio: {Studio_july * days:.2f} lv.")