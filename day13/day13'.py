from sympy import symbols, Eq, solve

button_a = []
button_b = []
prizes = []
with open('../inputs/day13.txt', 'r') as file:
    text = file.read()

lines = text.split('\n')
print(lines)


x, y = symbols('x y')
eq1 = Eq(x + y, 5)
eq2 = Eq(2 * x + 2 * y, 10)

result = solve((eq1, eq2), (x, y))
print(result)
