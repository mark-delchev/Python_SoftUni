people_num = int(input())
season = input()
if people_num <= 5:
    spring_price = 50
    summer_price = 48.5
    fall_price = 60
    winter_price = 86
else:
    spring_price = 48
    summer_price = 45
    fall_price = 49.5
    winter_price = 85

if season == "summer":
    price = people_num * summer_price
    price *= 0.85
elif season == "winter":
    price = people_num * winter_price
    price *= 1.08
elif season == "autumn":
    price = people_num * fall_price
elif season == "spring":
    price = people_num * spring_price
print(f"{price:.2f} leva.")