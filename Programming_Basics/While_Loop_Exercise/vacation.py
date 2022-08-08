needed_money = float(input())
available_money = float(input())
days_counter = 0
spending_counter = 0
while True:
    days_counter += 1
    type_of_action = input()
    if type_of_action == 'spend':
        money_spent = float(input())
        available_money -= money_spent
        spending_counter += 1
        if available_money < 0:
            available_money = 0
        if spending_counter == 5:
            print("You can't save the money.")
            print(days_counter)
            break
    elif type_of_action == 'save':
        money_saved = float(input())
        available_money += money_saved
        spending_counter = 0
    if available_money >= needed_money:
        print(f"You saved the money for {days_counter} days.")
        break
