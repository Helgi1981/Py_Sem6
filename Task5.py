# Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, 
# max_number.

# Пример:

# На входе:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# На выходе:
# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19


# 1. Решение через традиционный итератор:

def find_indices_traditional(lst, min_number, max_number):
    """Функция для нахождения индексов элементов, попадающих в заданный диапазон"""
    indices = []
    for i in range(len(lst)):
        if min_number <= lst[i] <= max_number:
            indices.append(i)
    return indices

# Заданные данные
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# Поиск и вывод индексов
indices = find_indices_traditional(list_1, min_number, max_number)
print("Индексы элементов, попадающих в диапазон:")
for index in indices:
    print(index)

"""
Пояснение:
1. Проходим по каждому элементу списка и проверяем, находится ли он в заданном диапазоне.
2. Если да, добавляем его индекс в список индексов.
"""


# 2. Решение с применением List Comprehension:

def find_indices_comprehension(lst, min_number, max_number):
    """Функция для нахождения индексов элементов, попадающих в заданный диапазон с использованием List Comprehension"""
    return [i for i in range(len(lst)) if min_number <= lst[i] <= max_number]

# Заданные данные
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# Поиск и вывод индексов
indices = find_indices_comprehension(list_1, min_number, max_number)
print("Индексы элементов, попадающих в диапазон:")
for index in indices:
    print(index)

"""
Пояснение:
Используем List Comprehension для создания списка индексов элементов, которые находятся 
в заданном диапазоне.
"""


# 3. Решение с использованием рекурсии:

def find_indices_recursive(lst, min_number, max_number, index=0, indices=None):
    """Рекурсивная функция для нахождения индексов элементов, попадающих в заданный диапазон"""
    if indices is None:
        indices = []
    if index == len(lst):
        return indices
    if min_number <= lst[index] <= max_number:
        indices.append(index)
    return find_indices_recursive(lst, min_number, max_number, index + 1, indices)

# Ввод данных
list_1 = list(map(int, input("Введите элементы списка через пробел: ").split()))
min_number = int(input("Введите минимальное значение диапазона: "))
max_number = int(input("Введите максимальное значение диапазона: "))

# Поиск и вывод индексов
indices = find_indices_recursive(list_1, min_number, max_number)
print("Индексы элементов, попадающих в диапазон:")
for index in indices:
    print(index)

"""
Пояснение:
1. Рекурсивная функция проверяет каждый элемент списка на соответствие диапазону и 
добавляет его индекс в список, если условие выполняется.
2. Функция рекурсивно вызывает себя для следующего индекса, пока не достигнет конца 
списка.
"""
