liked_meals = {}
disliked_meals = []
while True:
    command = input()
    if command == "Stop":
        break
    else:
        commands = command.split("-")
        if commands[0] == "Like":
            if commands[1] not in liked_meals.keys():
                liked_meals[commands[1]] = [commands[2]]
            else:
                if commands[2] not in liked_meals.values():
                    liked_meals[commands[1]].append(commands[2])
        elif commands[0] == "Dislike":
            if commands[1] not in liked_meals.keys():
                print(f"{commands[1]} is not at the party.")
            else:
                if commands[2] in liked_meals[commands[1]]:
                    disliked_meals.append(commands[2])
                    print(f"{commands[1]} doesn't like the {commands[2]}.")
                    for a in liked_meals.values():
                        try:
                            a.remove(commands[2])
                        except ValueError:
                            pass
                else:
                    print(f"{commands[1]} doesn't have the {commands[2]} in his/her collection.")

for key, value in liked_meals.items():
    print(f"{key}: {', '.join(value)}")

print(f"Unliked meals: {len(disliked_meals)}")



