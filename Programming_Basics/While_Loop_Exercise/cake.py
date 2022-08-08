cake_length = int(input())
cake_width = int(input())
cake_pieces = cake_width * cake_length
pieces_eaten = 0
while True:
    command = input()
    if command != 'STOP':
        command = int(command)
        pieces_eaten += command
    elif command == 'STOP':
        pieces_remaining = cake_pieces - pieces_eaten
        print(f'{pieces_remaining} pieces are left.')
        break
    if pieces_eaten > cake_pieces:
        pieces_needed = pieces_eaten - cake_pieces
        print(f'No more cake left! You need {pieces_needed} pieces more.')
        break

