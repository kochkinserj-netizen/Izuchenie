# Основы обработки ошибок: try, except, else, finally

# SyntaxError - Синтаксическая ошибка
# До запуска программы. Python не может разобрать код.
# print(4.lower())

# Exception - Исключение
# Во время выполнения. Код правильный, но операция невозможна.
# print(10/0) ZeroDivisionError: division by zero

ids = [1,2,3,4]
# print(ids[5]) #IndexError: list index out of range

# Стек вызовов (Traceback)
# traceback — «след» того, как код дошёл до ошибки.

def divide(a, b):
    return a / b

def main():
    divide(10, 0)

# main()


# Для обработки исключений
# try-except-else-finally

a = 10
b = 10

first_value = input("Введите число a: ")
print(f'Введено {first_value}')
second_value = input('Введите число b: ')
print(f'Введено {second_value}')

try:
    first_value_number = int(first_value)
    second_value_number = int(second_value)

    result = first_value_number / second_value_number
except ValueError:
    print('Неверное значение')
except ZeroDivisionError:
    # Перехватчик различных ошибок
    print('Нельзя делить на ноль')
else: # Что делать если нет ошибки
    print(result)
finally:   # Типичное применение — освобождение ресурсов (закрытие файла, соединения с БД, сетевых подключений).
    print('Программа полностью выполнена')




# Знакомство с синтаксическими ошибками и исключениями

# Синтаксические ошибки(SyntaxError) - ошибки парсинга
# интерпритатор не может понять написанный код
'''
if True
    print('error')
'''

# Исключения (Exception)
# возникают в синтаксически правильном коде

# ZeroDivisionError - ошибка деления на ноль
# print(1/0)

# NameError - обращение к несуществуещей переменной
# print(course)

# TypeError - операция к объекту несовмесимого типа
# print(1+'2')

# IndexError -выход запределы списка
lst =[]
# print(lst[10])

# ValueError - не найдено значение
# print(lst.index(5))

# KeyError - попытка получения несуществуещего ключа
user = {}
# print(user['name'])

# когда возникает ошибка, то программа завершается и в консоли появляется трасировка ошибки
# трасировка (Traceback) - это отображение места ошибки (файл,строка)

# Обработка исключений : try-except
#  try - попробывать что то сделать и если возникла ошибка то обработать ее в except

try:
    print(1/0)
except ZeroDivisionError:
    print('Ошибка деления на ноль')

# операции I/O
# try:
#     # number = int(input('Введите число: '))
#     # result =100/number
#     print(result)
# except ValueError as e:
#     print(f'Произошла ошибка {e}')
#     print(f'тип ошибки {type(e).__name__}')
# except ZeroDivisionError as e:
#     print(f'Произошла ошибка {e}')

# try-except-else-finally
# Код в блоке else выполнится только если в try не произошло исключений
# если они возникли то они обрабатыватываются в блоке except
# блок finally работает всегда, обычно используется для освобождение ресурсов (закрытия фалов, сетевых соедениний)
file = None

try:
    file = open('resume.txt', 'r')
except FileNotFoundError as e:
    print('Файл не найден')
    print(f'{e}')
else:
    # если файл есть будем читать его
    content = file.read()
    print(content)
    file.close()
finally:
    if file:
        file.close()


# BaseException -> Exception
# Exception -> ArithmaticError
# Exception -> TypeError
# Exception -> NameError
# Exception -> IndexError
# ArithmaticError -> ZeroDivisionError

# Что стоит оборачивать в try-except
# операции I/O
# Распаковка/парсинг JSON / XML / YAMP
# Приведение типов, конвертация
# Матиматические операции с плавующей точкой
# Сетевое взаимодействие (API - запросы. Запросы к БД)