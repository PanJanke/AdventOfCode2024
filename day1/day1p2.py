list1, list2 = [], []
sum = 0

with open('../inputs/day1.txt', 'r') as file:
    for line in file:
        col1, col2 = line.strip().split()
        list1.append(int(col1))
        list2.append(int(col2))

count_dict = {}

for num in list2:
    if num in count_dict:
        count_dict[num] += 1  # Increment the count
    else:
        count_dict[num] = 1  # Initialize count to 1



for num in list1:
    if num in count_dict:
        sum=sum+num*count_dict[num]

print(sum)