# Ветвления
# Знакомство с условиями

'''age = 8
# код проверяет возраст, если меньше 18 лет то доступа нет

if age >= 18:
    print('Access allowed')
else:
    print('Access denied')

# else - выполняется когда ни одно вырожение сверху не выполнилось здесь не нужно выражений

# взять пользовательский ввод буквы (a,b,c,d,e)

grade = 'A'
if grade == 'A':
    print('Отлично')
elif grade == 'B':
    print('Хорошо')
elif grade == 'C':
    print('Удолетворительно')
elif grade == 'D':
    print('Неудовлетворительно')
elif grade == 'E':
    print('Плохо, очень плохо')
else:
    print('Неверный ввод')

full_name = 'Sergei Kochkin'
if 's' in full_name.lower():
    print('letter s is present')
else:
    print('letter s is not present')

if 'b'  not in full_name.lower(): # Использование not для инверсии
    print('letter b is not present')
else:
    print('letter b is present')

role = ['admin', 'manager', 'user', 'quest']

user_role = input('Введите роль:')
if user_role in role:
    print('Допустимая роль')
else:
    print('Недопустимая роль ')

# Использование логического and

user_age = int(input('Введите возраст: '))
if user_age >= 18 and user_role in role:
    print('Access allowed')
else:
    print('Access denied')

# or - или

user_age = int(input('Введите возраст: '))
if user_age >= 18 or user_role in role:
    print('Access allowed')
else:
    print('Access denied')'''
from platform import android_ver

role = 'admin'
student_age = 23
is_course_paid = False

if role == 'admin' and student_age >= 18 or is_course_paid:
    print('Access allowed')
else:
    print('Access denied')

# Переменная которая хранит логический тип данных не нужно сравнивать
if is_course_paid:
    print('Курс оплачен')
else:
    print('Не оплачен')

# Приоритет логических элементов
# 1 - and
# 2 - or

