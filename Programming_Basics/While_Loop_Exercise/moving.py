width = int(input())
length = int(input())
height = int(input())
space = width * height * length
box_sum = 0
while True:
    command = input()
    if command == 'Done':
        space_remaining = space - box_sum
        print(f'{space_remaining} Cubic meters left.')
        break
    elif command != 'Done':
        box_num = int(command)
        box_sum += box_num
    if box_sum > space:
        space_needed = box_sum - space
        print(f'No more free space! You need {space_needed} Cubic meters more.')
        break


