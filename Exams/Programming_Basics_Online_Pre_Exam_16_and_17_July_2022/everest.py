meters_total = 5364
meters_needed = 8848
day_counter = 1
while True:
    com = input()
    if com == "Yes":
        day_counter += 1
    if day_counter > 5:
        print("Failed!")
        print(meters_total)
        break
    elif com == "END":
        print("Failed!")
        print(meters_total)
        break
    meters_climbed = int(input())
    meters_total += meters_climbed
    if meters_total > meters_needed:
        print(f"Goal reached for {day_counter} days!")
        break
