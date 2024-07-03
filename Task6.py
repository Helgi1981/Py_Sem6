# Заполните массив элементами арифметической прогрессии. Её первый элемент a1, 
# разность d и количество элементов n будет задано автоматически. Формула для получения 
# n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример:

# На входе:
# a1 = 2
# d = 3
# n = 4

# На выходе:
# 2
# 5
# 8
# 11

# 1. Решение через традиционный итератор

def arithmetic_progression_traditional(a1, d, n):
    """Функция для заполнения массива элементами арифметической прогрессии"""
    progression = []
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    return progression

# Заданные данные
a1 = 2
d = 3
n = 4

# Заполнение и вывод прогрессии
progression = arithmetic_progression_traditional(a1, d, n)
print("Элементы арифметической прогрессии:")
for element in progression:
    print(element)


# 2. Решение с применением List Comprehension

def arithmetic_progression_comprehension(a1, d, n):
    """Функция для заполнения массива элементами арифметической прогрессии с использованием List Comprehension"""
    return [a1 + i * d for i in range(n)]

# Заданные данные
a1 = 2
d = 3
n = 4

# Заполнение и вывод прогрессии
progression = arithmetic_progression_comprehension(a1, d, n)
print("Элементы арифметической прогрессии:")
for element in progression:
    print(element)


# 3. Решение с использованием рекурсии

def arithmetic_progression_recursive(a1, d, n, current=0, progression=None):
    """Рекурсивная функция для заполнения массива элементами арифметической прогрессии"""
    if progression is None:
        progression = []
    if current == n:
        return progression
    progression.append(a1 + current * d)
    return arithmetic_progression_recursive(a1, d, n, current + 1, progression)

# Заданные данные
a1 = 2
d = 3
n = 4

# Заполнение и вывод прогрессии
progression = arithmetic_progression_recursive(a1, d, n)
print("Элементы арифметической прогрессии:")
for element in progression:
    print(element)