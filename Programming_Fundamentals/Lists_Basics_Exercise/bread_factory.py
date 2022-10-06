energy = 100
coins = 100
events = input().split("|")
event_name = [i.split("-")[0] for i in events]
value_lst = [int(i.split("-")[1]) for i in events]
successful_day = True

for i in range(len(events)):
    value = value_lst[i]
    event = event_name[i]
    if event == "rest":
        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins < value:
            successful_day = False
            print(f"Closed! Cannot afford {event}.")
            break
        coins -= value
        print(f"You bought {event}.")

if successful_day:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")