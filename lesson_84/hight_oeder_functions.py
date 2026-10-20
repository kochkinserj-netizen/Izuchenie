# Функции как объекты первого класса
from collections.abc import Callable


def sey_hi(name: str) -> str:
    return f'Hello {name.title()}'


print(sey_hi('sergei'))


# Присваивание функции переменной

print(sey_hi)

def format_text(text: str) -> str:
    return text.title()

to_upper_case = format_text  # присваиваем функцию, не вызываем! (без скобок)
print(to_upper_case)
print(format_text)
print(to_upper_case("привет"))
print(to_upper_case("здравствуйте"))
print(to_upper_case("сергей"))
print(to_upper_case("Python"))
print(to_upper_case("pyThOn"))


# Передача функции как аргумента

def get_full_name(title_args: Callable[[str],[str]],first_name:str, last_name:str)-> str:
    return f'{title_args(first_name)} {title_args(last_name)}'

print(get_full_name(format_text,'sergei', 'kochkin'))

# Передача функции в sorted

words = ["Яблоко", "грУшА", "апельсин", "МаНдАрИн"]
# обычная сортировка не подойдет
words.sort()
print(words)

def transform_to_lower_case(fruit: str) -> str:
    return fruit.lower()


sorted_words = sorted(words, key=transform_to_lower_case)
print(sorted_words)

# Возврат функции из функции

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
print(add5(10))   # 15
print(add5(3))    # 8

add10 = make_adder(10)
print(add10(10))   # 20
print(add10(3))    # 13

# Функции в структурах данных

# Список функций

def square(x):
    return x * x


def cube(x):
    return x * x * x


transformations = [square, cube]
for func in transformations:
    print(func(3))   # 9, 27

    # Словарь команд


    def start_game():
        print("Игра началась!")


    def show_help():
        print("Справка: используйте команды start, help, quit")


    def quit_game():
        print("Выход из игры.")
        exit()


    commands = {
        "start": start_game,
        "help": show_help,
        "quit": quit_game
    }

    #
    # while True:
    #     cmd = input("Введите команду: ").strip().lower()
    #     if cmd in commands:
    #         commands[cmd]()  # вызываем функцию по ключу
    #     else:
    #         print("Неизвестная команда.")

# Функция, возвращающая функцию по имени

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def choose_operation(oper):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    return operations.get(oper)

mylt = choose_operation('*')
print(mylt)
print(mylt(2,6))