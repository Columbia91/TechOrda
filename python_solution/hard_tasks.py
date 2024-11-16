# 1. Сумма от 1 до n без циклов
def sum_1_n(n):
    return n * (n + 1) // 2

# 2. Подсчет високосных лет до заданного года n
def count_leap_year(n):
    leap_years = n // 4 - n // 100 + n // 400
    return leap_years

# 3. Замена первых 4 битов с остальными 4 битами
def swap_bits(a):
    return ((a & 0b00001111) << 4) | ((a & 0b11110000) >> 4)

# 4. Сортировка трех чисел без циклов
def sort_nums_three(a, b, c):
    return sorted([a, b, c])

# Массивы

# 5. Нахождение медианы
def median(array):
    if not array:
        return None
    array.sort()
    mid = len(array) // 2
    return array[mid - 1] if len(array) % 2 == 0 else array[mid]

# 6. Числа из второго массива, отсутствующие в первом
def miss_you(array1, array2):
    return sorted(set(array2) - set(array1))

# 7. Проверка на идеально сбалансированный элемент
def perfectly_balanced(array):
    total_sum = sum(array)
    left_sum = 0
    for num in array:
        if left_sum == (total_sum - left_sum - num):
            return True
        left_sum += num
    return False

# 8. Поиск пар для покупки акций
def stock_buy(m, prices):
    price_dict = {}
    for i, price in enumerate(prices):
        complement = m - price
        if complement in price_dict:
            return sorted([price_dict[complement], i])
        price_dict[price] = i

# Самая сложная задача функции

# 9. Ханойские башни
def hanoi_tower(n, source=1, target=3, auxiliary=2):
    if n == 1:
        print(f"Диск 1 с башни {source} переложить в башню {target}")
    else:
        hanoi_tower(n - 1, source, auxiliary, target)
        print(f"Диск {n} с башни {source} переложить в башню {target}")
        hanoi_tower(n - 1, auxiliary, target, source)

# использование функций
# 1. Сумма от 1 до n
print(sum_1_n(5))  # 15

# 2. Подсчет високосных лет
print(count_leap_year(100))  # 24

# 3. Замена битов
print(swap_bits(15))  # 240

# 4. Сортировка трех чисел
print(sort_nums_three(3, 2, 1))  # [1, 2, 3]

# 5. Нахождение медианы
print(median([1, 2, 3]))  # 2

# 6. Числа, отсутствующие в первом массиве
print(miss_you([1, 1, 3, 2, 5], [1, 3, 9, 1, 5, 7]))  # [7, 9]

# 7. Проверка на идеально сбалансированный элемент
print(perfectly_balanced([1, 2, 9, 8, 5, 7]))  # True

# 8. Поиск пар для покупки акций
print(stock_buy(8, [8, 7, 3, 1, 3, 10]))  # [1, 3]

# 9. Ханойские башни
hanoi_tower(2)
