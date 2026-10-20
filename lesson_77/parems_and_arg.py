# Параметры и аргументы:

'''Когда мы определяем функцию, мы перечисляем параметры – переменные, которые будут доступны внутри функции.
При вызове мы передаём аргументы – конкретные значения.
Самый простой способ – позиционные аргументы: значения присваиваются параметрам в том порядке, в котором они записаны.
'''

# Позиционные аргументы



def calc_sum(a, b):
    return a + b

calc_sum_result = calc_sum(2, 3)
print(calc_sum_result)



def get_full_name(first_name, last_name, patronymic):
    return f'{first_name} {patronymic} {last_name}'

svk = get_full_name('Sergei','Kochkin','Vladimirovich')
print(svk)



def diff(a, b):
    """Возвращает разность a - b."""
    return a - b

print(diff(5, 3))   # 2
print(diff(3, 5))   # -2

# распаковка списков и кортежей
params = [10, 3]
print(diff(*params))


# ключевые/ именовонные аргументы
# в таком случае можно явно указать какому параметру какое значение будет принадлежать
# keyword arguments

print(diff(b=15, a= 10))
print(diff(b=50, a=20))

print(get_full_name(last_name= 'Подушкин', first_name= 'Анатолий', patronymic='Евгеньевич'))


def get_numbers_sum(a,b,c,d):
    return a + b + c + d


# Вызов функции с позиционными и именовонными аргументами
# Именовоные идут после позиционных

print(get_numbers_sum(1,2,3,4))
print(get_numbers_sum(d=2, a=5, c=3, b=4))
print(get_numbers_sum(1, 15,20,d=30))
# print(get_numbers_sum(d=2, 5, c=3, b=4))

kwargs = {'a': 7, 'b': 4, 'c': 3, 'd': 2}
print(get_numbers_sum(**kwargs))   # 16



# Значеия по умолчанию


def greet(name="Гость"):
    """Приветствует пользователя, по умолчанию – Гость."""
    print(f"Привет, {name}!")

greet()          # Привет, Гость!
greet("Анна")    # Привет, Анна!


def rectangle_area(length, width=None):
    if width is None:
        width = length
    return length * width

print(rectangle_area(10,5))
print(rectangle_area(10))

# При работе значения по умолчанию определяются в конце списка всех парамметров

def get_user_info(name='Petr',surname='Ivanov',age=20):
    pass


# Значение выражения для default определяется один раз – в момент определения функции,
# а не при каждом вызове.

x = 10


def foo(a=x):
    return a


x = 20
print(foo())  # 10, потому что default вычислен на момент определения функции


# Для неизменяемых типов (числа, строки, кортежи, None) это безопасно.
# Но для изменяемых объектов (списки, словари, множества)
# это может привести к неочевидному поведению.



def add_item(item, lst=[]):   # очень плохая идея!
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]   <- список "запомнил" предыдущий элемент!
print(add_item(3))   # [1, 2, 3]   <- список "запомнил" предыдущий элемент!



def add_item_correct(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_correct(1))  # [1]
print(add_item_correct(2))  # [2]   <- каждый вызов создаёт новый список


def create_user(name, age, is_admin=False):
    return f"{name}, возраст {age}, администратор: {is_admin}"

# Варианты вызова:
print(create_user("Иван", 25))                    # позиционные
print(create_user("Анна", 30, is_admin=True))     # позиционные + ключевой
print(create_user(age=22, name="Пётр"))           # только ключевые (порядок не важен)
print(create_user("Мария", is_admin=True, age=28))# позиционный, потом ключевые (порядок среди ключевых любой)
# Ошибка: create_user(is_admin=True, "Сергей")     # SyntaxError: позиционный после ключевого