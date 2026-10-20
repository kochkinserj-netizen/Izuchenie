# Использование f-строк для форматирования

name = "Sergei"
patronymic = 'Vladimirovich'
surname = 'Kochkin'

full_name =name + " " + patronymic + " " + surname
print(full_name)

fio = f'{name} {patronymic} {surname}'
print(fio)

taecher = 'Vadim Zviagintsev'
coures = 'Python'
price = 30000
price_str = str(price)


course_info = 'Преподавателем курса'+ ' '+ coures + ' ' + 'является опытный преподаватель' + ' ' + taecher + '.' + '\n' + 'Цена курса' + ' ' + coures + ' ' + price_str
print(course_info)

course_info_formatted = f'Преподавателем курса {coures} является опытный преподаватель {taecher}. Цена курса {coures} {price_str}p.'
print(course_info_formatted)

# При форматировании строк можно выполнять вычесления
num1 = 10
num2 = 5
summa = f'{num1} + {num2} = {num1 + num2}'
substract = f'{num1} - {num2} = {num1 - num2}'
print(summa)
print(substract)

# Выполнение методов со строками
name = 'sergei'
surname = 'kochkin'
full_name = f'{name.capitalize()} {surname.capitalize()}'
print(full_name)