# Практика по работе с условиями

#


# [0-17] - access denied
# (-inf; 0) - возраст не может меньше 0
# [18;120] -access allowed
# [121; inf] - вы долгожитель

'''if user_age < 0:
    print('Возрост не может быть меньше 0')
elif 0 <= user_age < 12:
    print('Вы ребенок')
elif 12 <= user_age < 18:
    print('Вы подросток')
elif 18 <= user_age < 60 :
    print('Вы работяга')
elif 60 <= user_age < 120:
    print('Вы пенсионер')
else:
    print('Вы долгожитель')'''
from turtledemo.penrose import inflatedart

from unicodedata import digit

'''user_input = input('Type something: ')

if not user_input:
    print('Empty string')
else:
    print(user_input)'''

# status_code: 100, 200, 300, 400, 500
# информационные, успешные, перенаправление, ошибка клиента,ошибка сервиса, none_code

'''user_status_code = int(input('Введите статус код: '))
if user_status_code < 100 or user_status_code >= 600:
    print('Неизвесный статус код')
elif 100 <= user_status_code < 200:
    print('Информационный код')
elif 200 <= user_status_code < 300:
    print('Успешный код')
elif 300 <= user_status_code < 400:
    print('Перенаправление')
elif 400 <= user_status_code < 500:
    print('Ошибка клиента')
elif 500 <= user_status_code < 600:
    print('Ошибка сервера')
else:
    print('Вы ничего не ввели')'''

roles = ['admin', 'manager', 'user', 'quest']
# < 1 - новичок в роли
# до 3 опытный
# >3 мастер

user_role = input('Type yor role: ')
if user_role in roles:
    print(f'{user_role.capitalize()} присутствует в ролях')
    experiense_age = int(input('Сколько лет вы работаете на этой должности? '))
    if experiense_age < 0:
        print('Недопустимый ввод')
    elif experiense_age < 1:
        print(f'Вы новичок на озиции {user_role}')
    elif 1 <= experiense_age < 3:
        print(f' Вы опытный {user_role}')
    elif experiense_age >= 3 :
        print(f' Вы маститый {user_role}')
else:
    print('Недопустимая роль')
