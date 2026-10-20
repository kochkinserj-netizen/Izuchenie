# Проверка содержимого строки

# .startswifh() - начинается ли строка с указаного текста True False. Может применять кортеж

name = 'Sergei'
print(name.startswith('S'))
print(name.startswith('s'))
print(name.startswith('Sergei'))
print(name.startswith(('S', 'Sergei')))  # Кортеж обязательно еще в ()
print(name.startswith('S', 0 )) # префикс и старт не нужно писать
print(name.startswith('er', 1,3 ))

# .endswifh() - тоже что и предыдущее только с конца. Может применять кортеж

file = 'imege.jpg'
print(file.endswith('.jpg'))
print(file.endswith(('.jpeg','.jpg','png')))

website = 'www.google.com'
domain = ('.ru','.com','.net')  #tuple кортеж
print(website.endswith(domain))

surname = 'Kochkin'
suffix = 'n'
print(surname.endswith(suffix))

# .isdigit() - состоит строка из цифр? True & False ТОЛЬКО ЦИФРЫ 0-9

phone = '89127371098'
print(phone.isdigit())
print('12.2'.isdigit()) # точка не строка
age = '28'
print(age.isdigit())

# .isalpha - состоет ли строка из букв?

name = 'Sergei'
russian_name = 'Сергей'
print(name.isalpha())
print(russian_name.isalpha())  #не зависит от алфавита
print(''.isalpha())
print('Sergei Kochkin'.isalpha()) # Из за пробела False (пробел это не буква)

# isalnum() — состоит ли строка из букв и/или цифр

login = 'Sergei154'
print(login.isalnum())
nickname = 'Sergei'
print(nickname.isalnum())
year = '2018'
print(year.isalnum())
full_name = 'Sergei_Kochkin'
print(full_name.isalnum())

# isspace() — состоит ли строка только из пробельных символов
spase_str = '            '
print(spase_str.isspace())
empty_str = ''
print(empty_str.isspace())

full_name = 'Sergei\nKochkin'  # \n - символ переноса строки
print(full_name)

new_line = '\n'
print(new_line.isspace())

# \t - табуляция
fio = 'Kochkin\tSergei\tVladimirovich'
print(fio)
print(fio.isspace())

"""
"python3".isalpha() → False
"2025".isdigit() → True
"hello world".isalnum() → False
" \n".isspace() → True
"script.py".endswith(".py") → True
"Telegram".startswith(("Whats", "Tele")) → True
"""
print('python3'.isalpha())
print('2025'.isdigit())
print('hello world'.isalnum())
print(' \n'.isspace())
print('script.py'.endswith('.py'))
print('Telegram'.startswith(("Whats", "Tele")))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
