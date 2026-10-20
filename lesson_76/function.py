# Знакомство с функциями: определение и вызов

user_name_1 = 'Sergei'
user_surname_1 = 'Kochkin'
full_name_user1 = f'{user_name_1} {user_surname_1}'
print(full_name_user1)

user_name_2 = 'Harry'
user_surname_2 = 'Hannah'
full_name_user2 = f'{user_name_2} {user_surname_2}'
print(full_name_user2)

'''
def имя_функции():
    """Необязательная строка документации (docstring)"""
    действие 1
    действие 2
    return результат  # необязательно
'''

def greet():
    ''' Вывод приветствия'''
    print('Привет, студент!')

print(greet)
greet()

def griting():
    # pass - заглушка
    pass

print(greet())

# параметры и передача данных в функцию

def say_hello(name):
    """Приветствует пользователя по имени."""
    print(f"Привет, {name}!")

# аргументы - конкретные значения передающиеся в функцию
say_hello('Sergei')
say_hello('Сергей')
say_hello('Анатолий')

def get_full_name(first_name, last_name):
    print(f'{first_name} {last_name}')

get_full_name('Sergei', 'Kochkin')
get_full_name('Григорий', 'Подушкин')



# возврат значений return None

def calc_sum(num1, num2):
    return num1 + num2

result = calc_sum(4,6)
print(result)


print(calc_sum(12,5))

def calc_subtract(num1, num2):
    return num1 - num2
    print('Вычетание')  # Недостижимый код

result_subtract = calc_subtract(4,6)
print(result_subtract)


# return - результат выполнения функции

def get_user_info(name, surname, age):
    full_name = f'{name} {surname}'
    user_info = f'Пользователю {full_name} {age} лет'
    print(user_info)

get_user_info('Sergei', 'Kochkin', 30)

print(get_user_info('Sergei', 'Kochkin', 30)) # результат - None

user_info = get_user_info('Sergei', 'Kochkin', 30)
print(result)  # None



# Примеры использования функций
# условия
def max_of_two(x, y):
    """Возвращает большее из двух чисел."""
    if x > y:
        return x
    else:
        return y

greater_number = max_of_two(5, 6)
print(greater_number)

# циклы
def print_numbers(n):
    """Выводит числа от 1 до n."""
    for i in range(1, n + 1):
        print(i)

print_numbers(5)

# взятие пользовательского ввода
def ask_age():
    age = input("Сколько вам лет? ")
    print(f"Через 10 лет вам будет {int(age) + 10}")

# Приветствие с проверкой
def greet_polite(name, formal=False):
    if formal:
        return f"Здравствуйте, {name}!"
    else:
        return f"Привет, {name}!"

print(greet_polite("Иван"))           # Привет, Иван!
print(greet_polite("Анна", True))     # Здравствуйте, Анна!

# сумма диопазона
def sum_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

print(sum_range(10, 25))   # 15

# функция с условием
def guess_secret_number():
    secret = 7
    guess = int(input("Угадайте число от 1 до 10: "))
    if guess == secret:
        return "Верно!"
    elif guess < secret:
        return "Слишком мало"
    else:
        return "Слишком много"

# print(guess_secret_number())

def show_teacher_info():
    teacher_name = 'Vadim'
    teacher_surname = 'Zviagintsev'
    teacher_full_name = f'{teacher_name} {teacher_surname}'
    return teacher_full_name
print(show_teacher_info())
# переменные, объявленные в теле функции видны и доступны только внутри функции
# они недоступны извне
# print(teacher_name)