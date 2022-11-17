tasks = {}
i = 0

while True:
    command = input()
    if command == "stop":
        break
    if i % 2 == 0:
        key = command
    else:
        value = int(command)
        if key in tasks:
            tasks[key] += value
        else:
            tasks[key] = value
    i += 1

for key, value in tasks.items():
    print(f"{key} -> {value}")
