# Знакомство с оператарими match\case

status_code = int(input('Введите статус код из 400-й группы: '))

age = 20
if age < 18:
    print('Access denied')
else:
    print('Access allowed')

match age:
    case age if age < 18:
        print('Access denied')
    case _:
        print('Access denied')


# 400 - bad request
# 401 - unauthorized
# 403 - forbidden
# 404 - not found
# любой другой статус - incorrect status code

if status_code == 400:
    print('Bad Request')
elif status_code == 401:
    print('Unauthorized')
elif status_code == 403:
    print('Forbidden')
elif status_code == 404:
    print('Not Found')
else:
    print('Incorrect status code')

match status_code:
    case 400:
        print('Bad Request')
    case 401:
        print('Unauthorized')
    case 403:
        print('Forbidden')
    case 404:
        print('Not Found')
    case _:
        print('Incorrect status code')

# несколько значений в один кейс

# пн,вт,ср,чт,пт - будний день
# сб,вс - выходной

day = input('Введите день недели: ')

match day:
    case 'пн' | 'вт' | 'ср' | 'чт' | 'пт' :
        print('Будний день')
    case 'сб' | 'вс' :
        print('Будний день')
    case _:
        print('Недопустимый ввод')


user_age = int(input('Введите свой возраст: '))

if user_age < 0:
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
    print('Вы долгожитель')

match user_age:
    case user_age if user_age < 0:
        print('Возрост не может быть меньше 0')
    case user_age if 0 <= user_age < 12:
        print('Вы ребенок')
    case user_age if 12 <= user_age < 18:
        print('Вы подросток')
    case user_age if 18 <= user_age < 60 :
        print('Вы работяга')
    case user_age if 60 <= user_age < 120:
        print('Вы пенсионер')
    case _:
        print('Вы долгожитель')


