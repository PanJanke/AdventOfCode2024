from sympy import symbols, Eq, solve, sympify
import re

button_a_list = []
button_b_list = []
prizes = []
with open('../inputs/day13.txt', 'r') as file:
    text = file.read()

lines = text.split('\n')
# print(lines)
test = lines
button_a_list = []
button_b_list = []
desired_pos_list = []
for i, string in enumerate(lines):
    j = i % 4
    if j == 0:
        button_a_list.append(re.findall(r'\d+', string))
    elif j == 1:
        button_b_list.append(re.findall(r'\d+', string))
    elif j == 2:
        desired_pos_list.append(re.findall(r'\d+', string))
    elif j == 3:
        continue

sum = 0

for i in range(0, len(desired_pos_list)):
    button_a = button_a_list[i]
    button_b = button_b_list[i]
    desired_pos = desired_pos_list[i]
    first_eq_left = button_a[0] + ' * x +' + button_b[0] + '* y'
    first_eq_right = desired_pos[0]

    second_eq_left = button_a[1] + ' * x +' + button_b[1] + '* y'
    second_eq_right = desired_pos[1]

    x_sym, y_sym = symbols('x y')
    eq1 = Eq(sympify(first_eq_left), sympify(first_eq_right))
    eq2 = Eq(sympify(second_eq_left), sympify(second_eq_right))
    result = solve((eq1, eq2), (x_sym, y_sym))

    a = result[x_sym]
    b = result[y_sym]

    if "/" in str(a) or "/" in str(b):
        continue
    elif a < 0 or b < 0:
        continue
    else:
        sum += 3 * int(a) + int(b)
print(sum)
