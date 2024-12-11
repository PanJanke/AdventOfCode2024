def pos_of_x(arr):
    y = len(arr)
    x = len(arr[y - 1])
    result = []

    for j in range(0, y):
        for i in range(0, x):
            if arr[j][i] == 'X':
                result.append((j, i))

    return result


def count_occurences(words, pattern):
    counter = 0
    for word in words:
        counter = counter + word.count(pattern)
    return counter


# positive means for y=ax+b where a>0
def get_positive_diagonal(arr):
    height = len(arr)
    width = len(arr[height - 1])

    diag_list = []
    for a in range(0, height):
        x = 0
        y = a
        diag = []
        while x < width and y >= 0:
            diag.append(arr[y][x])
            x = x + 1
            y = y - 1
        diag_list.append("".join(diag))

    for a in range(1, width):
        x = a
        y = height - 1
        diag = []
        while x < width and y >= 0:
            diag.append(arr[y][x])
            x = x + 1
            y = y - 1
        diag_list.append("".join(diag))

    return diag_list


def get_negative_diagonal(arr):
    height = len(arr)
    width = len(arr[height - 1])

    diag_list = []
    for a in range(0, height):
        x = width - 1
        y = a
        diag = []
        while x >= 0 and y >= 0:
            diag.append(arr[y][x])
            x = x - 1
            y = y - 1
        diag_list.append("".join(diag))

    for a in range(width - 2, -1, -1):
        x = a
        y = height - 1
        diag = []
        while x >= 0 and y >= 0:
            diag.append(arr[y][x])
            x = x - 1
            y = y - 1
        diag_list.append("".join(diag))

    return diag_list


def columns_to_strings(array_2d):
    num_columns = len(array_2d[0]) - 1

    columns_as_strings = [
        "".join(array_2d[row][col] for row in range(len(array_2d)))
        for col in range(num_columns)
    ]

    return columns_as_strings


with open('../inputs/day4.txt', 'r') as file:
    array = [list(line) for line in file]

rows = []
with open('../inputs/day4.txt', 'r') as file:
    for line in file:
        rows.append(line)

columns = columns_to_strings(array)

diagonals_neg = get_negative_diagonal(array)
diagonals_pos = get_positive_diagonal(array)

counter = 0

counter = counter + count_occurences(columns, 'XMAS')
counter = counter + count_occurences(columns, 'SAMX')

counter = counter + count_occurences(rows, 'XMAS')
counter = counter + count_occurences(rows, 'SAMX')

counter = counter + count_occurences(diagonals_neg, 'XMAS')
counter = counter + count_occurences(diagonals_neg, 'SAMX')

counter = counter + count_occurences(diagonals_pos, 'XMAS')
counter = counter + count_occurences(diagonals_pos, 'SAMX')

print(counter)
