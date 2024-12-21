with open('../inputs/day8.txt', 'r') as file:
    array = [list(line.strip()) for line in file]


def find_antinodes(array, antenas):
    height = len(array)
    width = len(array[0])
    antinodes = [['.' for _ in range(width)] for _ in range(height)]
    antena_types = antenas.keys()

    for char in antena_types:
        amount = len(antenas[char])
        if amount > 1:
            for i in range(0, amount):
                for j in range(i + 1, amount):

                    pos_a = antenas[char][i]
                    pos_b = antenas[char][j]

                    y_diff = pos_a[0] - pos_b[0]
                    x_diff = pos_a[1] - pos_b[1]
                    y_anti = pos_b[0] + 2 * y_diff
                    x_anti = pos_b[1] + 2 * x_diff
                    if 0 <= y_anti < height and 0 <= x_anti < width:
                        antinodes[y_anti][x_anti] = '#'

                    y_diff = pos_b[0] - pos_a[0]
                    x_diff = pos_b[1] - pos_a[1]
                    y_anti = pos_a[0] + 2 * y_diff
                    x_anti = pos_a[1] + 2 * x_diff
                    if 0 <= y_anti < height and 0 <= x_anti < width:
                        antinodes[y_anti][x_anti] = '#'

    return antinodes


def set_empty_map(array):
    height = len(array)
    width = len(array[0])
    return [['.' for _ in range(width)] for _ in range(height)]


def get_atenas(array):
    antenas = {}
    for y, row in enumerate(array):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antenas:
                    antenas[char] = []
                antenas[char].append((y, x))
    return antenas


with open('../inputs/day8.txt', 'r') as file:
    array = [list(line.strip()) for line in file]

antenas = get_atenas(array)

antinodes = find_antinodes(array, antenas)

count = 0
for row in antinodes:
    count +=row.count('#')

print(count)
