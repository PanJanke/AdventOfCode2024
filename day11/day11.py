import copy

with open('../inputs/day11.txt', "r") as file:
    text = file.read()

stones = text.split()
result = []

for i in range(25):
    print('iteracja: ' + str(i))
    result.clear()
    for num in stones:
        partial = []

        if num == '0':
            partial.append('1')
        elif len(num) % 2 == 0:
            mid = int(len(num) / 2)
            left = num[0:mid]
            partial.append(left)
            right = num[mid:len(num)]
            right = right.lstrip('0')
            if len(right) == 0:
                right = '0'
            partial.append(right)
        else:
            multiply = int(num) * 2024
            partial.append(str(multiply))


        result.extend(partial)
    stones = copy.deepcopy(result)
    print(len(stones))
    #print(stones)

