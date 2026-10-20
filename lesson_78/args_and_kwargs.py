# Знакомство с *args и **kwargs: произвольное количество аргументов

def calc_sum(a,b,c,d=0, e=0):
    return a+b+c+d+e


print(calc_sum(1,2,3))


# args- аргументы
# *args - в теле вункции аргументы будут передоватсся кортежем
def sum_calc(*args):
    print(sum(args))
    total = 0
    for arg in args:
        total += arg
    return total
sum_calc(1,2,3,4,5,6,7)


numbers_list = [10,11,12,13,14]


# function(*iterable) - распаковка
print(calc_sum(*numbers_list))



def greet(greeting, *names):
    print(greeting)
    print(names)
    for name in names:
        print(f"{greeting}, {name}!")

greet("Здравствуйте", "Анна", "Иван", "Мария","Михаил")
# Привет, Анна!
# Привет, Иван!
# Привет, Мария!

# kwargs- keyword argument - именованные аргументы
# **kwargs – словарь произвольного числа именованных аргументов



def get_profile_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

get_profile_info(name="Анна", age=25, city="Москва", occupation = "Python Developer", salary=200_000)
# name: Анна
# age: 25
# city: Москва
# occupation: Python Developer
# salary: 200000


user = {
    'user_id':102,
    'name':'Sergo',
    'surname':'Koch',
    'age':25,
}


def get_user_info(user_id, name, surname, age):
    for k, v in user.items():
        print(f"{k}: {v}")

# function(**dict)- распаковка словаря
get_user_info(**user)



# Совместное использование параметров разных типов
# def func(обычные, *args, ключевые_со_значением_по_умолчанию, **kwargs):

def order_pizza(size, *toppings, delivery=False, **extra):
    print(f"Пицца размера: {size}")
    print(f"Топпинги: {', '.join(toppings) if toppings else 'нет'}")
    print(f"Доставка: {'да' if delivery else 'нет'}")
    for key, value in extra.items():
        print(f"{key}: {value}")

# Вызовы
order_pizza("Большая", "грибы", "ветчина", delivery=True, комментарий="без лука")
order_pizza("Маленькая")   # без топпингов и доставки
order_pizza("Средняя", "сыр", "помидоры", адрес="ул. Ленина", этаж=3)



def wrapper(func, *args, **kwargs):
    """Вызывает func с переданными аргументами и возвращает результат."""
    result = func(*args, **kwargs)
    return result

def add(a, b):
    return a + b

print(wrapper(add, 3, 5))            # 8
print(wrapper(add, a=10, b=20))          # 30




# Напишите функцию log_call(func, *args, **kwargs),
# которая печатает имя функции и переданные аргументы,
# затем вызывает func(*args, **kwargs) и возвращает результат.

def log_call(func, *args, **kwargs):
    pass






















try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")
finally:
    print("Блок finally выполняется всегда")

