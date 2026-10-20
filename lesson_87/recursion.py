# Рекурсия

def greeting():
    print("Привет")

greeting()

# Рекурсивная функция — это функция, которая вызывает саму себя.

def countdown(n: int) :
    if n <= 0:                 # базовый случай
        print("Пуск!")
    else:
        print(n)
        countdown(n - 1)       # рекурсивный случай с уменьшенным аргументом

countdown(10)

# Факториал числа n (обозначается n!) — это произведение всех натуральных чисел от 1 до n

def fact(n: {__eq__}):
    if n == 0:          # базовый случай
        return 1
    else:
        return n * fact(n - 1)  # рекурсивный вызов

print(fact(5))  # 120
print(fact(32)) # 263130836933693530167218012160000000

# Переворот строки (рекурсивно)
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("привет"))  # "тевирп"

# Палиндром (проверка строки)

def is_palindrome(s):
    # Приводим к нижнему регистру для корректного сравнения (опционально)
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("Анна"))      # True
print(is_palindrome("Потоп"))     # True
print(is_palindrome("Привет"))    # False