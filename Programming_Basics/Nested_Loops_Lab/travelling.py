money_saved = 0
while True:
    destination = input()
    if destination == "End":
        break
    money_needed = float(input())
    while money_saved < money_needed:
        money_saved += float(input())
    if money_saved >= money_needed:
        print(f"Going to {destination}!")
        money_saved = 0

