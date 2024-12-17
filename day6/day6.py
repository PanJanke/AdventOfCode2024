def find_player_pos(array_2d, char):
    for row_index, row in enumerate(array_2d):
        for col_index, cell in enumerate(row):
            if cell == char:
                return (row_index, col_index)
    return None


def get_char(pos):
    if is_player_inside(pos):
        return array[pos[0]][pos[1]]
    else:
        return '.'


def turn_right(value):
    match value:
        case "^":
            return ">"
        case ">":
            return "v"
        case "v":
            return "<"
        case "<":
            return "^"
        case _:
            return value


def destination(pos, dir):
    x = pos[0]
    y = pos[1]

    match dir:
        case "^":
            return (x, y - 1)
        case ">":
            return (x + 1, y)
        case "v":
            return (x, y + 1)
        case "<":
            return (x - 1, y)
        case _:
            return pos


def is_player_inside(pos):
    x = pos[0]
    y = pos[1]
    if y < 0 or y >= height or x < 0 or x >= width:
        return False
    else:
        return True


with open('../inputs/day6.txt', 'r') as file:
    array = [list(line.strip()) for line in file]

array = [list(row) for row in zip(*array)]

height = len(array[0])
width = len(array)

direction = '^'
pos = find_player_pos(array, direction)

while True:
    current_pos = pos
    dest = destination(pos, direction)
    dest_char = get_char(dest)

    if dest_char == '#':
        direction = turn_right(direction)
    else:
        pos = dest
        if not is_player_inside(pos):
            break
        else:
            array[pos[0]][pos[1]] = "X"

count = sum([row.count('X') for row in array])
print(count + 1)  # xd
