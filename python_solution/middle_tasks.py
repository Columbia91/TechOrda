# 1. Проверка четности числа
def check_even_odd(number):
    if number % 2 == 0:
        return "Число четное."
    else:
        return "Число нечетное."

# 2. Проверка, является ли строка палиндромом
def is_palindrome(string):
    string = string.lower().replace(" ", "")  # Удаляем пробелы и приводим к нижнему регистру
    if string == string[::-1]:
        return "Строка является палиндромом."
    else:
        return "Строка не является палиндромом."

# 3. Проверка, является ли число простым
def is_prime(number):
    if number <= 1:
        return "Число не является простым."
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "Число не является простым."
    return "Число является простым."

# 4. Проверка корректности даты
def is_valid_date(date_str):
    from datetime import datetime
    try:
        day, month, year = map(int, date_str.split('.'))
        datetime(year, month, day)  # Проверяем корректность даты
        return "Дата корректная."
    except ValueError:
        return "Дата некорректная."

# 5. Нахождение совершенных чисел в диапазоне
def perfect_numbers_in_range(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if num > 1 and sum(i for i in range(1, num) if num % i == 0) == num:
            perfect_numbers.append(num)
    return perfect_numbers

# 6. Проверка, является ли число числом Фибоначчи
def is_fibonacci(number):
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number

# 7. Проверка, является ли число совершенным
def is_perfect_number(number):
    if number > 1 and sum(i for i in range(1, number) if number % i == 0) == number:
        return "Число является совершенным."
    else:
        return "Число не является совершенным."

# 8. Определение сезона по дате
def determine_season(month, day):
    if (month == 12) or (month <= 2):
        return "Зима"
    elif (month >= 3 and month <= 5):
        return "Весна"
    elif (month >= 6 and month <= 8):
        return "Лето"
    elif (month >= 9 and month <= 11):
        return "Осень"

# использование функций
# 1. Проверка четности
print(check_even_odd(4))

# 2. Проверка палиндрома
print(is_palindrome("A man a plan a canal Panama"))

# 3. Проверка простого числа
print(is_prime(29))

# 4. Проверка даты
print(is_valid_date("20.01.2002"))

# 5. Совершенные числа в диапазоне
print(perfect_numbers_in_range(0, 1000))

# 6. Проверка Фибоначчи
print(is_fibonacci(25))

# 7. Проверка совершенного числа
print(is_perfect_number(28))

# 8. Определение сезона
print(determine_season(1, 15))  # Зима
print(determine_season(4, 10))  # Весна
print(determine_season(7, 20))  # Лето
print(determine_season(10, 5))  # Осень
