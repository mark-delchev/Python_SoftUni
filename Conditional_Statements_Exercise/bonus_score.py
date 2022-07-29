number = int(input())
bonus = 0
bonus2 = 0

if number <= 100:
    bonus = 5
elif 100 < number < 1000:
    bonus = number * 0.20
elif number > 1000:
    bonus = number * 0.10

if number % 2 == 0:
    bonus2 = 1
elif number % 10 == 5:
    bonus2 = 2

print(bonus + bonus2)
print(number + bonus + bonus2)


