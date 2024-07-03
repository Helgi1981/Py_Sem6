# Задача №4. Решение в группах

# Два различных натуральных числа n и m называются дружественными, если сумма делителей 
# числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – 
# дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не 
# превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую пару не дает).

# Ввод: 300
# Вывод: 220 284


# 1. Решение через традиционный итератор:

def sum_of_divisors(n):
    """Функция для вычисления суммы делителей числа n (исключая само число)"""
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_amicable_numbers_traditional(k):
    """Функция для поиска всех пар дружественных чисел до k"""
    amicable_pairs = []
    checked = set()
    
    for n in range(2, k + 1):
        if n in checked:
            continue
        m = sum_of_divisors(n)
        if m != n and m <= k and sum_of_divisors(m) == n:
            amicable_pairs.append((n, m))
            checked.add(n)
            checked.add(m)
    
    return amicable_pairs

# Ввод данных
k = int(input("Введите натуральное число k: "))

# Поиск и вывод дружественных чисел
amicable_pairs = find_amicable_numbers_traditional(k)
print("Пары дружественных чисел до", k, ":")
for n, m in amicable_pairs:
    print(n, m)

"""
Пояснения:

Функция sum_of_divisors(n):
1. Начинаем с суммы равной 1, так как 1 всегда является делителем.
2. Проходим по всем числам от 2 до квадратного корня из n.
3. Если число является делителем, добавляем его и его соответствующую пару (если это не 
одно и то же число).

Функция find_amicable_numbers(k):
1. Создаем пустой список для пар дружественных чисел.
2. Создаем множество checked для отслеживания уже проверенных чисел.
3. Проходим по всем числам от 2 до k.
4. Для каждого числа находим сумму его делителей.
5. Проверяем, что найденное дружественное число не равно самому числу, не превышает k, 
и его сумма делителей равна исходному числу.
6. Если условия выполняются, добавляем пару в список и отмечаем числа как проверенные.

Основная часть:
1. Вводим значение k.
2. Вызываем функцию find_amicable_numbers и выводим найденные пары.
"""

# 2. Решение с применением List Comprehension:

def sum_of_divisors(n):
    """Функция для вычисления суммы делителей числа n (исключая само число)"""
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_amicable_numbers_comprehension(k):
    """Функция для поиска всех пар дружественных чисел до k с использованием List Comprehension"""
    amicable_pairs = [
        (n, m)
        for n in range(2, k + 1)
        for m in [sum_of_divisors(n)]
        if m != n and m <= k and sum_of_divisors(m) == n and n < m
    ]
    return amicable_pairs

# Ввод данных
k = int(input("Введите натуральное число k: "))

# Поиск и вывод дружественных чисел
amicable_pairs = find_amicable_numbers_comprehension(k)
print("Пары дружественных чисел до", k, ":")
for n, m in amicable_pairs:
    print(n, m)

"""
Пояснение:
1. Используем List Comprehension для создания списка пар дружественных чисел.
2. Проверяем условия в одном выражении.
"""


# 3. Решение с использованием рекурсии:

def sum_of_divisors(n):
    """Функция для вычисления суммы делителей числа n (исключая само число)"""
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_amicable_pairs_recursive(n, k, checked, pairs):
    """Рекурсивная функция для поиска пар дружественных чисел"""
    if n > k:
        return pairs
    if n not in checked:
        m = sum_of_divisors(n)
        if m != n and m <= k and sum_of_divisors(m) == n:
            pairs.append((n, m))
            checked.add(n)
            checked.add(m)
    return find_amicable_pairs_recursive(n + 1, k, checked, pairs)

def find_amicable_numbers_recursive(k):
    return find_amicable_pairs_recursive(2, k, set(), [])

# Ввод данных
k = int(input("Введите натуральное число k: "))

# Поиск и вывод дружественных чисел
amicable_pairs = find_amicable_numbers_recursive(k)
print("Пары дружественных чисел до", k, ":")
for n, m in amicable_pairs:
    print(n, m)

"""
Пояснение:
1. Рекурсивная функция перебирает числа от 2 до k.
2. Проверяет условия для дружественных чисел и добавляет их в список пар.
3. Использует множество checked для отслеживания уже проверенных чисел.
"""
