def is_order_safe(order, rules):
    for i in range(0, len(order)):
        num = order[i]
        for j in range(i + 1, len(order)):

            if num not in rules or order[j] not in rules[num]:
                return False
    return True


dict_rules = {}
orders = []
with open('../inputs/day5.txt', 'r') as file:
    for line in file:
        if line.strip() == "":
            break
        tab = line.strip().split("|")

        if tab[0] not in dict_rules:
            dict_rules[tab[0]] = []
        dict_rules[tab[0]].append(tab[1])

    for line in file:
        orders.append(line.strip().split(','))

sum = 0
for order in orders:
    if is_order_safe(order, dict_rules):
        sum = sum + int(order[len(order) // 2])

print(sum)
