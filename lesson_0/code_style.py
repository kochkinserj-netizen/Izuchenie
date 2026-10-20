# Python Code Style

# 1. Имена переменных и функций
teacher_name = 'Vadim'
student_name = 'Sergei'
course_price = 30_000

def get_full_name(name,surname):
    """
    :param name:
    :param surname:
    :return:
    """
    return f'{name} {surname}'

# 2. Константы
PI=3.14
URL= 'russian-it-akademy.ru'
ADULT_AGE = 18
# 3. Отступы
# 4. Длина строки

def  make_greeting(user_name):
    """
    :param user_name:
    :return:
    """
    return f'Hello {user_name}'

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return f'{self.name} {self.surname}'


num_1 = 5
num_2 = 4
multiplication = num_1 * num_2
print(multiplication)

user_age  = int(input('Введите свой возраст'))

if user_age >= ADULT_AGE:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')




