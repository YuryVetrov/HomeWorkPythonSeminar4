# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
from collections import defaultdict
with open('Task5.1_HWPS4.txt', 'w') as file:
    # Запишем первый многочлен 2x^3 + 6x^2 - 2x - 3 в виде кортежей 
    p1 = [(2,3),(6,2),(-2, 1),(-3,0)]
    for el in p1:
        file.write(f'{el}')

with open('Task5.1_HWPS4.txt', 'r') as file:
    read_file = file.read()
    q1 = read_file.split(',')
print(q1)

with open('Task5.2_HWPS4.txt', 'w') as file:
    # Запишем второй многочлен -4x^3 + 2x^2 + 2x - 7 в виде кортежей 
    p2 = [(-4,3),(2,2),(2,1),(7,0)]
    for el in p2:
        file.write(f'{el}')

with open('Task5.2_HWPS4.txt', 'r') as file:
    read_file = file.read()
    q2 = read_file.split(',')
print(q2)

def combine(q1, q2):
    total = defaultdict(int)
    for coefficient, exponent in q1 + q2:
        total[exponent] += coefficient
    return [item[::-1] for item in total.items()]
q1, q2 = p1, p2
print(combine(p1, p2))

with open('Task5.3_HWPS4.txt', 'w') as file:
    file.write(f'{combine(p1, p2)}')
