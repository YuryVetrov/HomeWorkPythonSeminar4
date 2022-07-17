# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей 
# числа N.
n = int(input('Введите любое число N = '))
def primeFactors(n):
    c = 2
    while(n > 1):
        if(n % c == 0):
            print(c, end=" ")
            n = n / c
        else:
            c = c + 1
primeFactors(n)
