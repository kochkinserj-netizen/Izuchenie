from typing import Union, List, NoReturn, Tuple, Dict, Callable


# Документирование: docstrings и аннотации типов

# Docstring (documentation string) – это строковый литерал,
# расположенный сразу после заголовка функции (или класса, модуля).
# Он описывает, что делает функция, какие параметры принимает и что возвращает.

# Функция возвращает полное имя пользователя
def get_full_name(first_name, last_name):
    """
    Возврощает полное имя пользователя

    :param first_name: str - имя пользователя
    :param last_name: str - фамилия пользователя

    :return: str -  f-строка полного имени
    """
    return f'{first_name} {last_name}'


print(get_full_name('Sergo', 'Koch'))
print(get_full_name(last_name='Doy',first_name='John'))

# Просмотр документации через атрибут __doc__
print(get_full_name.__doc__)
#  через функцию help()
help(get_full_name)



def divide(a, b):
    """Делит число a на число b.

    Args:
        a (float): Делимое.
        b (float): Делитель, не должен быть равен нулю.

    Returns:
        float: Частное от деления a на b.

    Raises:
        ZeroDivisionError: Если b равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b

print(get_full_name(14, 40))


# Type hints (Аннотация типов)

def greeting(name,surname):
    return f'{name} is {surname}'

# Аннотации типов – это синтаксис, позволяющий указать ожидаемые типы аргументов
# и возвращаемого значения прямо в заголовке функции.


def greet(name : str,surname : str) -> str :
    '''
    Приветствуем пользователя
    :param name: str - имя пользователя
    :param surname: str - фамилия пользователя

    :return: str - строка приветсвия
    '''

    return f'{name.strip().title()}  {surname.strip().title()}'



scool = 'Школа Вадима Звягинцева'
scool.strip()

print(greet('sergo', 'koch'))

print(greet.__doc__)

print(greet('S', 'koch'))


def square_root(x: Union[int,float]) -> float:
    return x ** 0.5

print(square_root(5))
print(square_root(10.15))

def square_root(x: int | float) -> float:
    return x ** 0.5


first_name: str = 'Sergo'
age: int = 30
salary: float = 330_000.50
is_married: bool = True
undefiend: None = None

def sum_calculator(numbers: List[int | float]) -> int | float:
    '''

    :param numbers:
    :return:
    '''
    return sum(numbers)

print(sum_calculator([1, 2, 3, 4, 5]))

companies = ('Yandex', 'TBank', 'Ozon')

# NoReturn - функция ничего не возвращает
def show_companies(comps: Tuple[str,str,str]) -> str:
    for c in comps:
        print( f'Я работаю в {c}')

show_companies(companies)

user = {
    'user_id':123,
    'name':'Bob',
    'surname':'McKinley',
    'salary': 330_000.53
}

# def show_user_info(data: Dict[str, Union[str, int, float]]):

def show_user_info(data: Dict[str, str | int | float]):
    for k, v in data.items():
        print(f'{k} -> {v}')

show_user_info(user)

def multiplication(x: int, y: int) -> int:
    return x * y

def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
   print(isinstance(x, int | float))
   print(isinstance(y, int | float))
   return func(x, y)

print(apply(multiplication, 2.0, 3.0))

