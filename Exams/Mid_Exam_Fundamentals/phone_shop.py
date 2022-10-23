phones = input().split(", ")
while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    elif command[0] == "Add":
        if command[1] in phones:
            continue
        else:
            phones.append(command[1])
    elif command[0] == "Bonus phone":
        bonus_phones = command[1]
        lst_bonus_phones = bonus_phones.split(":")
        old_phone = lst_bonus_phones[0]
        new_phone = lst_bonus_phones[1]
        if old_phone in phones:
            position = phones.index(old_phone)
            phones.insert(position + 1, new_phone)
    elif command[0] == "Remove":
        if command[1] in phones:
            phones.remove(command[1])
    elif command[0] == "Last":
        if command[1] in phones:
            phones.remove(command[1])
            phones.append(command[1])
print(", ".join(phones))