# Вложенные функции и замыкания

# Вложенные функции (Nested functions)

course = 'Python'

def outer():
    name = 'Sergei'
    def inner(): # вложенная функция
        print(name)
        print(course)


def outer_function(greeting):

    def inner_function(user_name):
        return f'{greeting} {user_name}'

    return inner_function

greet = outer_function('Hello')
print(greet('Sergei'))
print(greet('Vadim'))

def func():
    print('func')

copy_func = func
copy_func()


# Замыкание — это функция, которая запоминает значения переменных из объемлющей области видимости,
# даже после того, как внешняя функция завершила выполнение.

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

counter1 = outer() # count = 0
counter2 = outer() # count = 0

print(counter1()) # 1
print(counter1()) # 2
print(counter1()) # 3

print(counter2()) # 1
print(counter2()) # 2

# Логгер с уровнем важности
def make_logger(level):
    """Создаёт функцию-логгер, которая добавляет уровень важности к сообщениям."""
    def logger(message):
        print(f"[{level}] {message}")
    return logger

info = make_logger('INFO')
warn = make_logger('WARNING')
error = make_logger('ERROR')

info('Запрос на авторизацию получен')
info('Запрос на изменение данных выполнен')

warn('Устаревшая версия Node.js')

# Фабрика HTML-тегов
def make_tag(tag):
    """Возвращает функцию, оборачивающую текст в указанный тег."""
    def wrap(text):
        return f"<{tag}>{text}</{tag}>"
    return wrap

h1 = make_tag("h1")
p = make_tag("p")
div = make_tag("div")

print(h1('Изучение Python'))
print(p('Сегодня мы изучаем тему работы с замыканиями и вложеными функциями'))
print(div("Контейнер"))
