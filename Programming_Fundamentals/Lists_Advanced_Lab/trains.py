wagons = int(input())
wagons_lst = [0] * wagons
while True:
    command = input().split(" ")
    if command[0] == "End":
        break
    elif command[0] == "add":
        people = int(command[1])
        wagons_lst[-1] += people
    elif command[0] == "insert":
        people = int(command[2])
        index = int(command[1])
        last_people = wagons_lst[index]
        wagons_lst[index] = last_people + people
    elif command[0] == "leave":
        people = int(command[2])
        index = int(command[1])
        last_people = wagons_lst[index]
        wagons_lst[index] = last_people - people
print(wagons_lst)
        
