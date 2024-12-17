from itertools import product


def evaluate_left_to_right(numbers, operations):
    print(numbers)
    operations.pop(0)
    print(operations)
    result = int(numbers[0])
    for i, op in enumerate(operations):
        next_number = int(numbers[i + 1])
        if op == '+':
            result += next_number
        elif op == '*':
            result *= next_number
    return int(result)


def generate_combinations(operations, options):
    # Find positions of 'x' in the list
    x_positions = [i for i, op in enumerate(operations) if op == 'x']

    # Generate all possible combinations for the 'x' positions
    replacements = product(options, repeat=len(x_positions))

    # Replace 'x' with the generated options
    results = []
    for replacement in replacements:
        temp_operations = operations[:]
        for i, pos in enumerate(x_positions):
            temp_operations[pos] = replacement[i]
        results.append(temp_operations)

    return results


def edge_cases_check(numbers, result):
    res = int(result)
    max_val = 1
    min_val = 0
    for number in numbers:
        max_val *= int(number)
        min_val += int(number)
    if max_val < res or min_val > res:
        return False
    else:
        return True


def get_all_combinations(numbers, result):
    possible_operations = []
    for number in numbers:
        if int(result) % int(number) != 0:
            possible_operations.append('+')
        else:
            possible_operations.append('x')

    options = ['+', '*']
    return generate_combinations(possible_operations, options)


equations = []
with open('../inputs/day7.txt', 'r') as file:
    for line in file:
        equations.append(line)

sum = 0
for equation in equations:
    result = int(equation.split(':')[0])
    numbers = equation.split(':')[1].split()
    if not edge_cases_check(numbers, result):
        continue

    combinations = get_all_combinations(numbers, result)


    for comb in combinations:
        value = evaluate_left_to_right(numbers, comb)

        if value == result:
            sum += value
            break
print(sum)