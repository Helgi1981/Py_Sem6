# Задача №3. Решение в группах

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую 
# необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод:
# 1 2 3 2 3
# Вывод:
# 2


# 1. Решение через традиционный итератор с использованием словаря:

def count_pairs_traditional(arr):
    element_count = {}
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    pairs = 0
    for count in element_count.values():
        pairs += count // 2

    return pairs

# Ввод данных
arr = list(map(int, input("Введите элементы списка через пробел: ").split()))

# Вывод результата
print("Количество пар элементов, равных друг другу:")
print(count_pairs_traditional(arr))

"""
Пояснение:
1. Создаем словарь для подсчета количества каждого элемента.
2. Проходим по массиву и увеличиваем счетчик для каждого элемента в словаре.
3. Считаем количество пар, деля количество каждого элемента на 2 и суммируя результаты.
"""


# 2. Решение с применением collections.Counter:

from collections import Counter

def count_pairs_counter(arr):
    element_count = Counter(arr)
    return sum(count // 2 for count in element_count.values())

# Ввод данных
arr = list(map(int, input("Введите элементы списка через пробел: ").split()))

# Вывод результата
print("Количество пар элементов, равных друг другу:")
print(count_pairs_counter(arr))

"""
1. Используем Counter для подсчета количества каждого элемента.
2. Считаем количество пар, деля количество каждого элемента на 2 и суммируя результаты.
"""


# 3. Решение с использованием рекурсии:

def count_pairs_recursive(arr, element_count=None, index=0):
    if element_count is None:
        element_count = {}
    
    if index >= len(arr):
        return sum(count // 2 for count in element_count.values())
    
    num = arr[index]
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1
    
    return count_pairs_recursive(arr, element_count, index + 1)

# Ввод данных
arr = list(map(int, input("Введите элементы списка через пробел: ").split()))

# Вывод результата
print("Количество пар элементов, равных друг другу:")
print(count_pairs_recursive(arr))

"""
Пояснение:
1. Базовый случай: если достигнут конец массива, возвращаем сумму пар.
2. Обрабатываем текущий элемент, увеличивая счетчик в словаре.
3. Рекурсивно вызываем функцию для следующего элемента.
"""
