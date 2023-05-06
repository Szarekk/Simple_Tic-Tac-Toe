def print_game(matrix):
    print(f'''---------
    | {' '.join(matrix[0])} |
    | {' '.join(matrix[1])} |
    | {' '.join(matrix[2])} |
    ---------''')


def take_input():
    while True:
        x, y = input().split()
        if not (x.isdigit() and y.isdigit()):
            print('You should enter numbers!')
        elif not (int(x) in range(1, 4) and int(y) in range(1, 4)):
            print('Coordinates should be from 1 to 3!')
        elif matrix[int(x) - 1][int(y) - 1] != '_':
            print('This cell is occupied! Choose another one!')
        else:
            return int(x) - 1, int(y) - 1


def check_for_end(matrix):
    game = ''.join(matrix[0]) + ''.join(matrix[1]) + ''.join(matrix[2])
    rows = [game[:3], game[3:6], game[6:]]  # converting matrix to string then slicing it to get lines
    columns = [game[::3], game[1::3], game[2::3]]
    diagonals = [game[::4], game[2:7:2]]
    all_lines = rows + columns + diagonals
    if 'XXX' in all_lines:
        print('X wins')
        return True
    elif 'OOO' in all_lines:
        print('O wins')
        return True
    elif '_' not in game:
        print('Draw')
        return True
    return False


matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
player = 'X'
print_game(matrix)
while not check_for_end(matrix):
    x, y = take_input()
    matrix[x][y] = player
    print_game(matrix)
