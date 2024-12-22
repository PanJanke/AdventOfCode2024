def remove_dots(list):
    while list[len(list) - 1] == '.':
        list.pop()
    return list


with open('../inputs/day9.txt', "r") as file:
    text = file.read()

length = len(text)
index = 0
is_file = True
memory = []
for i in range(0, length):
    if is_file:
        for j in range(0, int(text[i])):
            memory.append(index)
        index += 1
        is_file = False
    else:
        for j in range(0, int(text[i])):
            memory.append('.')
        is_file = True

index = 0
memory = remove_dots(memory)
length = len(memory)

while index < len(memory):
    if memory[index] == '.':
        memory[index] = memory[len(memory) - 1]
        memory.pop()
        memory = remove_dots(memory)
    index += 1

count = 0
for i, num in enumerate(memory):
    count += i * int(num)
print(count)
