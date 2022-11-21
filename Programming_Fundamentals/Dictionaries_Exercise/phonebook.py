info = []
info_dict = {}
n = 0
while True:
    command = input()
    if not command.isnumeric():
        info += command.split("-")
    else:
        n = int(command)
        break

for i in range(0, len(info), 2):
    key = (info[i])
    value = info[i + 1]
    info_dict[key] = value


for names in range(n):
    name = input()
    for key, value in info_dict.items():
        if key == name:
            print(f"{key} -> {value}")
            break
    else:
        print(f"Contact {name} does not exist.")


