starting_height = 5364
everest = 8848
day_counter = 1
while starting_height < everest:
    command = input()
    if command == "END":
        print("Failed!")
        print(starting_height)
        break
    climbed_height = int(input())
    if command == "Yes":
        day_counter += 1
    if day_counter > 5:
        print("Failed!")
        print(starting_height)
        break
    starting_height += climbed_height
if starting_height >= everest:
    print(f"Goal reached for {day_counter} days!")
