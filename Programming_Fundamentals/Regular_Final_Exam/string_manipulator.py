string = input()
while True:
    command = input()
    if command == "End":
        break
    else:
        commands = command.split(" ")
        if commands[0] == "Translate":
            string = string.replace(commands[1], commands[2])
            print(string)
        elif commands[0] == "Includes":
            print(commands[1] in string)
        elif commands[0] == "Start":
            print(string.startswith(commands[1]))
        elif commands[0] == "Lowercase":
            string = string.lower()
            print(string)
        elif commands[0] == "FindIndex":
            print(string.rfind(commands[1]))
        elif commands[0] == "Remove":
            start_index = int(commands[1])
            stop_index = start_index + int(commands[2])
            string = string[0: start_index:] + string[stop_index::]
            print(string)


