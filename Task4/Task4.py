# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен 
# степени k.
#Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
#f(x) == 2*x^2 + 7*x - 18
#f(4) == 2*16 + 7*4 - 18 = 42
def generate_polynomial(degree, a, b):
    coefficients = [0] + [random.randint(1, 10) for _ in range(degree-1)]
    y = sum(coefficient * a**n for n, coefficient in enumerate(coefficients))
    coefficients[0] = b - y
    return coefficients
seq = generate_polynomial(3, 4, 42)
print(seq)

with open('task4_HWPS4.txt', 'w') as file:
    file.write(f'{seq}')
