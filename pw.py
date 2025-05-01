def factorial_recursive(n):
    """
    Обчислює факторіал числа n рекурсивно.
    """
    if n < 0:
        raise ValueError("Факторіал визначено лише для невід'ємних чисел.")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    """
    Обчислює n-те число Фібоначчі рекурсивно.
    """
    if n < 0:
        raise ValueError("Числа Фібоначчі визначені лише для невід'ємних чисел.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_list_recursive(lst):
    """
    Обчислює суму елементів списку рекурсивно.
    """
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])


def is_palindrome_recursive(s):
    """
    Перевіряє, чи є рядок паліндромом, рекурсивно.
    """
    import re
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


# === Приклади використання ===

print("Факторіал 5:", factorial_recursive(5))  # 120
print("10-те число Фібоначчі:", fibonacci_recursive(10))  # 55
print("Сума списку [1, 2, 3, 4, 5]:", sum_list_recursive([1, 2, 3, 4, 5]))  # 15
print("Чи є 'А роза упала на лапу Азора' паліндромом?:", is_palindrome_recursive("А роза упала на лапу Азора"))  # True
print("Чи є 'Привіт' паліндромом?:", is_palindrome_recursive("Привіт"))  # False
