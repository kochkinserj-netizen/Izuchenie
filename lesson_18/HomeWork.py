# Решение задач метда replase()

'''
Задача 1: Очистка данных
Есть строка с ценами, где вместо точек используются запятые, а в конце стоит символ валюты. Приведите её к формату с точками и без символа валюты.

# Исходная строка
price = "25,50$"
# Должно быть: 25.50
'''

price = "25,50$"
print(price
        .replace(",",".")
        .replace("$",""))

'''
Задача 2: Нормализация телефонного номера
Пользователь ввёл номер телефона с различными разделителями. Приведите его к формату без разделителей.

# Исходная строка
phone = " +7 (123) 456-78-90 "
# Должно быть: +71234567890
'''
phone = " +7 (123) 456-78-90 "
new_phone = (phone
             .replace(" ", "")
             .replace("-", "")
             .replace("(", "")
             .replace(")", ""))
print(new_phone)

'''
Задача 3: Обработка логинов
Удалите пробелы в начале и конце логина, а также замените пробелы внутри логина на подчёркивания.

# Исходная строка
username = "  john doe smith  "
# Должно быть: john_doe_smith
'''
username = "  john doe smith  "
new_username = username.strip().replace(" ", "_")
print(new_username)

'''
Задача 4: Чистка текста от лишних символов
В тексте есть лишние точки и пробелы в начале и конце. Очистите его.

# Исходная строка
text = "....   Hello World!   ....."
# Должно быть: Hello World!
'''
text = "....   Hello World!   ....."
new_text = text.replace(".",'').strip()
print(new_text)

'''
Задача 5: Форматирование пути файла
Уберите лишние слеши в начале и конце пути к файлу.

# Исходная строка
file_path = "///documents/report.txt///"
# Должно быть: documents/report.txt
'''
file_path = "///documents/report.txt///"
new_file_path = file_path.strip('/')
print(new_file_path)

'''
Задача 6: Обработка CSV-значений
В CSV-файле некоторые значения обернуты в кавычки и имеют пробелы. Очистите их.

# Исходная строка
csv_value = "  \"product name\"  "
# Должно быть: product name
'''
csv_value = "  \"product name\"  "
new_csv_value = csv_value.strip().replace("\"",'')
print(new_csv_value)

'''
Задача 7: Удаление определённых префиксов и суффиксов
Удалите определённые префиксы и суффиксы из строки.

# Исходная строка
text = "XXXHello WorldXXX"
# Должно быть: Hello World
'''
text = "XXXHello WorldXXX"
new_text = text.rstrip('X').lstrip('X')
print(new_text)

'''
Задача 8: Замена нескольких вариантов написания
Замените различные варианты написания "colour" на "color".

# Исходная строка
text = "My favourite colour is red. The colour blue is nice."
# Должно быть: "My favourite color is red. The color blue is nice."
'''
text = "My favourite colour is red. The colour blue is nice."
new_text = text.replace('colour','color')
print(new_text)

'''
Задача 9: Комплексная очистка данных
Очистите строку от лишних символов с обеих сторон и замените разделители внутри.

# Исходная строка
data = "  [[value1, value2, value3]]  "
# Должно быть: value1; value2; value3
'''

data = "  [[value1, value2, value3]]  "
new_data = data.strip().replace("[","").replace("]","")
print(new_data)