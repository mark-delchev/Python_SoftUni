puzzle = 2.60
doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

trip = float(input())
puzzle_a = int(input())
doll_a = int(input())
teddy_bear_a = int(input())
minion_a = int(input())
truck_a = int(input())

price = puzzle * puzzle_a + \
        doll * doll_a + teddy_bear * teddy_bear_a + \
        minion * minion_a + \
        truck * truck_a
orders = puzzle_a + doll_a + teddy_bear_a + minion_a + truck_a

if orders >= 50:
    new_price = price - price * 0.25
    profit = new_price - new_price * 0.10
    if profit >= trip:
        print(f'Yes! {profit-trip:.2f} lv left.')
    else:
        print(f'Not enough money! {trip-profit:.2f} lv needed.')
else:
    profit = price - price * 0.10
    if profit >= trip:
        print(f'Yes! {profit-trip:.2f} lv left.')
    else:
        print(f'Not enough money! {trip-profit:.2f} lv needed.')


#Изпуснах равното при orders и се чудех що не става, мамка му!
