# 1. int-cmp
def int_cmp(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

# 2. max-of-three
def max_of_three(a, b, c):
    return max(a, b, c)

# 3. sqr-sum-1-n
def sqr_sum_1_n(n):
    return sum(i ** 2 for i in range(1, n + 1))

# 4. print-even-a-b
def print_even_a_b(a, b):
    return [i for i in range(a, b + 1) if i % 2 == 0]

# 5. pow-a-b
def pow_a_b(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# 6. calc-deposit
def calc_deposit(n, k, b):
    for _ in range(n):
        b += b * (k / 100)
    return round(b, 2)

# 7. Min
def min_array(array):
    return min(array) if array else 0

# 8. range
def create_range(n):
    return list(range(1, n + 1))

# 9. sum
def sum_array(array):
    return sum(array)

# 10. sort
def sort_array(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# использование функций
# int-cmp
print(int_cmp(1, 0))  # 1

# max-of-three
print(max_of_three(42, 1, 0))  # 42

# sqr-sum-1-n
print(sqr_sum_1_n(3))  # 14

# print-even-a-b
print(print_even_a_b(0, 4))  # [0, 2, 4]

# pow-a-b
print(pow_a_b(2, 6))  # 64

# calc-deposit
print(calc_deposit(1, 5, 1000))  # 1050.0

# Min
print(min_array([1, 2, 3]))  # 1
print(min_array([]))  # 0

# range
print(create_range(5))  # [1, 2, 3, 4, 5]

# sum
print(sum_array([7, 5, 9, 1, 4]))  # 26

# sort
print(sort_array([7, 5, 9, 1, 4]))  # [1, 4, 5, 7, 9]