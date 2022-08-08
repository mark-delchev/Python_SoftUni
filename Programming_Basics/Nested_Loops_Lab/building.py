floors = int(input())
rooms = int(input())
room_name = ""
room_number = 0
for i in reversed(range(1, floors + 1)):
    for k in range(0, rooms):
        room_number = i * 10 + k
        if i == floors:
            room_name = f"L{room_number}"
        elif i % 2 == 0:
            room_name = f"O{room_number}"
        elif i % 2 != 0:
            room_name = f"A{room_number}"
        print(room_name, end=" ")
    print()






