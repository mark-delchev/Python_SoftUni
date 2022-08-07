age = int(input())
washing_machine = float(input())
toy_price = int(input())
toys = 0
money = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys += 1
for x in range(2, age + 1, 2):
    money += 10 * (x / 2) - 1

toys_profit = toys * toy_price
total_savings = toys_profit + money

if total_savings >= washing_machine:
    print(f'Yes! {total_savings - washing_machine:.2f}')
else:
    print(f'No! {washing_machine - total_savings:.2f}')




