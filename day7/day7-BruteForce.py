# BruteForce TOO SLOW

from itertools import permutations, product

equations = []
with open('../inputs/day7.txt', 'r') as file:
    for line in file:
        equations.append(line)

result = equations[0].split(':')[0]
numbers = equations[0].split(':')[1].split()

operations = ['+', '*']

sum = 0


def evaluate_left_to_right(numbers, operations):
    result = int(numbers[0])
    for i, op in enumerate(operations):
        next_number = int(numbers[i + 1])
        if op == '+':
            result += next_number
        elif op == '*':
            result *= next_number
    return result


def check_equation(numbers, result):
    # check edges
    res = int(result)
    max_val = 1
    min_val = 0
    for number in numbers:
        max_val *= int(number)
        min_val += int(number)
    if max_val < res or min_val > res:
        return 0

    for perm in permutations(numbers):
        # Generate all combinations of operations for (n - 1) positions
        for ops in product(operations, repeat=len(numbers) - 1):
            # Build the expression dynamically
            expr = f"{perm[0]}"
            for i, op in enumerate(ops):
                expr += f" {op} {perm[i + 1]}"
            # Evaluate the expression
            value = evaluate_left_to_right(perm, ops)

            if int(value) == int(result):
                return int(result)

    return 0


length = len(equations)
counter = 0
for equation in equations:
    result = equation.split(':')[0]
    numbers = equation.split(':')[1].split()
    sum = sum + check_equation(numbers, result)
    counter += 1
    print(str(counter) + '/' + str(length))
print(sum)
