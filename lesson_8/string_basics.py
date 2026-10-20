# Основы работы со строками str
# строка это любая последовательность заключенная в ковычки, ('') ("") (""" """)
# строка неизменяемая

teacher = "Vadim Zvyagincev"

name = 'Sergei'
print(name)

surname = "Kochkin"
print(surname)

# Разные ковычки эквиволентны

text = '''
Многострочный текст
сейчас он как коментарий
'''
print(text)

# str неизменяемый тип данных
fio = 'кочкин сергей владимирович'
print(fio.title())
print(fio)
# т.е. модифицируя стороки исходные данные не меняются

#  чтобы знгачение поменялось нужно заново присвоить результат операции
fio = fio.title()
print(fio)

# Операции со строками

# сложение строк (конкатенация)
full_name = name +' '+ surname # пробел для разрыва при выводе (что бы слова не слипались)
print(full_name)

user_name = 'Mihail'
user_surname = 'Kochkin'
user_patronymic = 'Sergeevich'
user_full_name = user_name +' '+ user_surname +' '+ user_patronymic
print(user_full_name)

# умнажение строк
lang = 'Python'
triple_lang = lang * 3
print(triple_lang)

# len(string) - метод для взятия длинны строки
# len - length

print(name)
print(len(name))

emtpty_string = ''
print(len(emtpty_string))

print(full_name)
print(len(full_name))  # пробелы тоже считает (считает все пробелы)

spaces_str = '     '
print(len(spaces_str))
