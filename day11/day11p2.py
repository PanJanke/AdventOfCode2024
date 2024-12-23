import copy

with open('../inputs/day11.txt', "r") as file:
    text = file.read()

stones = text.split()
result = []
memo = {}
for i in range(75):
    print('iteracja: ' + str(i))
    result.clear()
    for num in stones:
        partial = []
        if num not in memo:
            if num == '0':
                partial.append('1')
                memo[num] = partial
            elif len(num) % 2 == 0:
                mid = int(len(num) / 2)
                left = num[0:mid]
                partial.append(left)
                right = num[mid:len(num)]
                right = right.lstrip('0')
                if len(right) == 0:
                    right = '0'
                partial.append(right)
                memo[num] = partial
            else:
                multiply = int(num) * 2024
                partial.append(str(multiply))
                memo[num] = partial


        result.extend(memo[num])
    stones = copy.deepcopy(result)
print(len(stones))
    # print(stones)
