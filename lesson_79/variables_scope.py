import builtins

# Области видимости и правило LEGB

name = 'Sergo'

def get_user_name():
    name = 'John'
    print(name)


print(name)
get_user_name()
print(name)

# print(age)
# NameError: name 'age' is not defined

surname = 'Koch'

def get_user_surname():
    print(surname)
    # surname = 'Petrov'
    # UnboundLocalError: cannot access local variable 'surname' where it is not associated with a value

get_user_surname()


# Локальная область (Local)

# Когда вы определяете функцию, все переменные,
# которым присваивается значение внутри неё, локальны.
# Они живут только во время выполнения функции и недоступны извне.


def greet():
    message = "Привет!"   # локальная переменная
    print(message)


greet()

# NameError
# print(message)

def square(x):
   print(x)
   return x * x


print(square(10))
# print(x)  #NameError
# Локальные переменные создаются заново при каждом вызове функции и удаляются после её завершения.
# Это изолирует код и позволяет использовать одинаковые имена в разных функциях без конфликтов.

language = 'Python'

def show_prog_lang():
    language = 'GO'
    print(language)

print(language)
show_prog_lang()

# Важно: присваивание переменной внутри функции делает её локальной,
# даже если в глобальной области есть переменная с таким же именем.
# Но если вы только читаете переменную,
# Python будет искать её по правилу LEGB




# Глобальная область (Global)

# Переменные, определённые на уровне модуля (вне всех функций),
# находятся в глобальной области видимости.
# Они доступны для чтения из любой функции этого модуля.

app_name = "MyApp"   # глобальная переменная


def show_app_name():
    print(app_name)  # читаем глобальную переменную, ошибки нет
# Сначало ищем переменную в локальной области видимости
# если ее там нет то тогда читаем глобальную переменную

show_app_name()  # MyApp

# def show_unexisted_var():
#     print(u)
#
# show_unexisted_var()
# NameError: name 'u' is not defined

# Но изменить глобальную переменную внутри функции просто присваиванием нельзя –
# будет создана локальная переменная с тем же именем:

country = 'Russia'


def country_operation():
    country = 'France'
    print(country)


country_operation()
print(country)

counter = 0


def increment():
    global counter
    counter = 1   # создаёт ЛОКАЛЬНУЮ переменную counter, global дает поменять глобальную переменную из функции
    print(counter)

increment()
print(counter)

# Оператор global говорит Python: «имя counter в этой функции ссылается на глобальную переменную,
# не создавай локальную».
# Обычно использование global стараются минимизировать,
# так как оно усложняет понимание кода.
# Лучше возвращать новые значения или использовать изменяемые объекты (списки, словари), но с global нужно быть знакомым




# Объемлющие функции(Enclosing) и nonlocal

def outer():
    x = 10

    # объемлющая переменная для inner
    def inner():
        print(x)  # доступ на чтение

    inner()

outer()   # 10



count = 10

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner

f = outer()
print(f())   # 1
print(f())   # 2


# nonlocal ищет имя в ближайшей объемлющей области,
# пропуская локальную, но не доходя до глобальной.
# Если переменная не найдена в enclosing-областях,
# будет ошибка SyntaxError

# Применение: фабрики (создание функций с сохранённым состоянием),
# замыкания, счётчики. Это основа для декораторов,
# которые мы будем изучать позже.




# Встроенные имена (Built-in)
# В Python есть множество встроенных функций и констант:
# print, len, range, int, True, None и др.
# Они живут в built-in области видимости,
# которая автоматически загружается при запуске интерпретатора.

# Мы можем их читать отовсюду.
# Но очень не рекомендуется создавать переменные с такими же именами –
# это перекроет доступ к встроенной функции.

sum = 10
print(sum)

# print(sum([1,2,3]))  # TypeError: 'int' object is not callable

sum_func = builtins.sum


print(sum_func([1,2,3,4]))



# Правило LEGB

'''
Когда Python встречает имя в коде, он ищет его в следующем порядке:
Local – локальная область (внутри текущей функции).
Enclosing – объемлющие функции (если текущая функция вложена во внешние).
Global – глобальная область модуля.
Built-in – встроенная область.

Поиск останавливается на первом найденном имени.

Local -> Enclosing -> Global -> Built-in

'''



ages = [12,23,45]

def change_age():
    ages.append(60)
    pass
change_age()
print(ages)