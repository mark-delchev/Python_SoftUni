commands = input().split("||")
fuel = int(input())
ammunition = int(input())
#command_value = [int(i.split(" ")[1]) for i in commands]
command_str = [i.split(" ")[0] for i in commands]

for i in range(len(command_str)):
    if command_str[i] == "Travel":
        command_value_lst = commands[i].split(" ")
        command_value = int(command_value_lst[1])
        if command_value > fuel:
            print("Mission failed.")
            break
        else:
            fuel -= command_value
            print(f"The spaceship travelled {command_value} light-years.")
    elif command_str[i] == "Enemy":
        command_value_lst = commands[i].split(" ")
        command_value = int(command_value_lst[1])
        if ammunition >= command_value:
            ammunition -= command_value
            print(f"An enemy with {command_value} armour is defeated.")
        elif fuel >= command_value * 2:
            fuel -= command_value
            print(f"An enemy with {command_value} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif command_str[i] == "Repair":
        command_value_lst = commands[i].split(" ")
        command_value = int(command_value_lst[1])
        ammunition_added = command_value * 2
        fuel_added = command_value
        fuel += fuel_added
        ammunition += ammunition_added
        print(f"Ammunitions added: {ammunition_added}.")
        print(f"Fuel added: {fuel_added}.")
    else:
        print("You have reached Titan, all passengers are safe.")
