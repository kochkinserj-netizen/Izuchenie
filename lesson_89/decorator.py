# Декораторы
from functools import wraps
# Функции как объекты первого класса
def greet(name: str) -> str:
    print(f'Hello {name}')

say_hello = greet

greet('Sergei')

# Функция внутри функции

def outer():
    print('outer')

    def inner():
        print('inner')

    inner()

funky = outer

funky()


# Первый декоратор

# Декоратор — это функция, которая принимает другую функцию,
# расширяет или изменяет её поведение без изменения её исходного кода,
# и возвращает новую функцию.

def decorator_function(func):

    def wrapper():
        print('Действие ДО вызова функции')
        func()
        print("Действие ПОСЛЕ вызова функции")

    return wrapper


def say_hi():
    print('Hi! Nice to meet you!')


# Вручную применяем декоратор

decorator_say_hi = decorator_function(say_hi)
decorator_say_hi()

# В работе декораторы добавляются серез символ @

@decorator_function
def say_goodbye():
    print('goodbye')
say_goodbye()

# аналогично записи
# say_goodbye = decorator_function(say_goodbye)

# Что бы сделать уневирсальный декоратор во wrapper *ards , *kwargs
def decorator(func):
    @wraps(func) #
    def wrapper(*args, **kwargs):
        print('>>> DO <<<')
        result = func(*args, **kwargs)
        print('>>> POSLE <<<')
        return result
    return wrapper


# Декоратор не отработает потому что у вложенной фуекции нет доступа к аргументам
'''
@decorator_function
def get_full_name(name: str, surname: str):
    return f'{name} {surname}'

get_full_name('sergei', 'kochkin')
'''

@decorator
def get_full_name(name: str, surname: str):
    return f'{name} {surname}'



print(get_full_name('sergei', 'kochkin'))

print(get_full_name.__name__)







# Шпаргалка: Идеальный шаблон декоратора
# Скопируй этот код и используй как заготовку для любых будущих декораторов:

from functools import wraps
def my_template_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Код ДО выполнения функции
        result = func(*args, **kwargs)
        # Код ПОСЛЕ выполнения функции
        return result
    return wrapper