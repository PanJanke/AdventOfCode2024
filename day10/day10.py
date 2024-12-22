import copy
def check(y, x, height):
    if height == 9:
        global array
        global count
        array[y][x] = -1
        count += 1
        return

    # right
    if x + 1 < x_range:
        if int(array[y][x + 1]) == height + 1:
            check(y, x + 1, height + 1)
    # left
    if x - 1 >= 0:
        if int(array[y][x - 1]) == height + 1:
            check(y, x - 1, height + 1)
    # up
    if y - 1 >= 0:
        if int(array[y - 1][x]) == height + 1:
            check(y - 1, x, height + 1)
    # down
    if y + 1 < y_range:
        if int(array[y + 1][x]) == height + 1:
            check(y + 1, x, height + 1)


def find_zeroes(array):
    zeroes_list = []
    for y, line in enumerate(array):
        for x, num in enumerate(line):
            if int(array[y][x]) == 0:
                zeroes_list.append((y, x))
    return zeroes_list


with open('../inputs/day10.txt', 'r') as file:
    map = [list(line.strip()) for line in file]


zero_list = find_zeroes(map)
count = 0
x_range = len(map[0])
y_range = len(map)

for pos in zero_list:
    array = copy.deepcopy(map)
    y, x = pos
    check(y, x, 0)
print(count)
