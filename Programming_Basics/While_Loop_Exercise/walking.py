goal = 10000
steps_sum = 0
while True:
    command = input()
    if command != 'Going home':
        steps = int(command)
        steps_sum += steps
    elif command == 'Going home':
        steps_home = int(input())
        steps_sum += steps_home
        if steps_sum < goal:
            print(f'{goal - steps_sum} more steps to reach goal.')
            break
    if steps_sum >= goal:
        print('Goal reached! Good job!')
        print(f'{steps_sum - goal} steps over the goal!')
        break




