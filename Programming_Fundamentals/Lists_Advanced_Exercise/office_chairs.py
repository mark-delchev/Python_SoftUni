rooms = int(input())
total_visitors = 0
total_chairs = 0
no_chairs = False
for i in range(1, rooms + 1):
    chairs = input().split(" ")
    chairs_available = ([len(chairs[index]) for index in range(0, len(chairs), 2)])
    visitors = ([int(chairs[index]) for index in range(1, len(chairs), 2)])
    total_visitors += visitors[0]
    total_chairs += chairs_available[0]
    if visitors[0] > chairs_available[0]:
        print(f"{visitors[0] - chairs_available[0]} more chairs needed in room {i}")
        no_chairs = True
if total_chairs >= total_visitors and not no_chairs:
    print(f"Game On, {total_chairs - total_visitors} free chairs left")
    
