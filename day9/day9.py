def find_dots(text):
    result = []
    j = 0
    i = 0
    while (i < len(text)):
        if text[i] == '.':
            while (text[i + j] == '.'):
                j += 1
            result.append((i, j))
            i = i + j - 1
            j = 0
        i = i + 1

    return result


with open('../inputs/day9.txt', "r") as file:
    text = file.read()

length = len(text)
index = 0
is_file = True
memory = ''
for i in range(0, length):
    if is_file:
        for j in range(0, int(text[i])):
            memory += str(index)
        index += 1
        is_file = False
    else:
        for j in range(0, int(text[i])):
            memory += '.'
        is_file = True
print(memory)

gap_list = find_dots(memory)
print(gap_list)
print(len(memory))


for gap in gap_list:
    print(gap)
    l = len(memory)
    index, size = gap
    size = gap[1]
    candidate = memory[l - size:l]

    print(candidate)
    break
