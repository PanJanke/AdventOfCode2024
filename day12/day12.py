import copy

with open('../day12-2.txt', 'r') as file:
     map = [list(line.strip()) for line in file]

def print_maps(map):
    print("---------")
    for row in map:
        print(row)


y_len = len(map)
x_len = len(map[0])
island_counter = 0

map_visited = [[0 for _ in range(y_len)] for _ in range(x_len)] # 0 - non visited 1-first island etc
map_perimeter = [[0 for _ in range(y_len)] for _ in range(x_len)]
perimeter_sum = 0

def find_next_unvisited():
    for y in range(y_len):
        for x in range(x_len):
            if map_visited[y][x] == 0:
                return (y,x)
    return None

def check_node(y,x):

    map_visited[y][x] = island_counter
    c = map[y][x]
    same_neighbors = 0
    # up
    if y-1 >= 0:
        if map[y-1][x] == c:
            same_neighbors += 1
            if map_visited[y-1][x] == 0:
                check_node(y-1,x)
    # down
    if y+1 < y_len:
        if map[y+1][x] == c:
            same_neighbors += 1
            if map_visited[y+1][x] == 0:
                check_node(y+1,x)
    # left
    if x-1 >= 0:
        if map[y][x-1] == c:
            same_neighbors += 1
            if map_visited[y][x-1] == 0:
                check_node(y,x-1)
    # right
    if x+1 < x_len:
        if map[y][x+1] == c:
            same_neighbors += 1
            if map_visited[y][x+1] == 0:
                check_node(y,x+1)
    global perimeter_sum
    perimeter_sum += 4 - same_neighbors
    map_perimeter[y][x] = 4 - same_neighbors


result = 0

while find_next_unvisited() is not None:
    perimeter_sum = 0
    island_counter+=1
    pos = find_next_unvisited()
    y, x = pos
    check_node(y,x)
    result += perimeter_sum * sum(row.count(island_counter) for row in map_visited)

print(result)
#print_maps(map)
#print_maps(map_visited)
#print_maps(map_perimeter)






