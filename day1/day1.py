list1, list2 = [], []
sum = 0

with open('../inputs/day1.txt', 'r') as file:
    for line in file:
        col1, col2 = line.strip().split()
        list1.append(int(col1))
        list2.append(int(col2))

list1.sort()
list2.sort()

for i in range(len(list1)):
    sum = sum + abs(list1[i] - list2[i])

print(sum)