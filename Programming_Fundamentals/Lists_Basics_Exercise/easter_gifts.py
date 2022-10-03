gifts = input().split(" ")


while True:
    command = input()
    if command == "No Money":
        break
    else:
        command_lst = command.split(" ")
        item = command_lst[1]
    if command_lst[0] == "OutOfStock":
        for idx, i in enumerate(gifts):
            if i == item:
                gifts[idx] = None

        
    elif command_lst[0] == "Required":
        item_replace = command_lst[2]
        if 0 <= int(item_replace) < len(gifts):
            gifts[int(item_replace)] = item
    elif command_lst[0] == "JustInCase":
        gifts[-1] = item

gifts_final = [x for x in gifts if x != None]

print(" ".join(gifts_final))


