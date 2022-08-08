import sys
min_number = sys.maxsize
while min_number > -sys.maxsize:
    command = input()
    if command == "Stop":
        break
    current_num = int(command)
    if current_num < min_number:
        min_number = current_num
print(min_number)

