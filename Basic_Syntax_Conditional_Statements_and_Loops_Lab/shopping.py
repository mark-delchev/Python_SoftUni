budget = int(input())
money_spent = 0
while True:
    command = input()
    if command == "End":
        break
    else:
        purchase = int(command)
        money_spent += purchase
        if money_spent > budget:
            print("You went in overdraft!")
            break
if money_spent <= budget:
    print("You bought everything needed.")
