import sys
max_number = -sys.maxsize
while max_number < sys.maxsize:
    try:
        current_number = int(input())
    except ValueError:
        break
    if current_number > max_number:
        max_number = current_number
print(max_number)




