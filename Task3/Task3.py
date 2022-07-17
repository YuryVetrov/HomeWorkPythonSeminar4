# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.
nums = list(map(str,input('Введите числа списка через пробел ').split()))
def print2SingleNumbers(nums):
    set1 = set()
    n = len(nums)
    for i in nums:
        if i in set1:
            set1.remove(i)
        else:
            set1.add(i)
    print("Неповторяющиеся элементы списка : " + " ".join(map(str, set1)))
print2SingleNumbers(nums)