import sys
max_number = -sys.maxsize
while max_number < sys.maxsize:
    command = input()
    if command == "Stop":
        break
    current_number = int(command)
    if current_number > max_number:
        max_number = current_number
print(max_number)