# Задача 5 (Регистр)
# Дана строка: text = "PyThOn Is A pOpUlAr LaNgUaGe"
# Преобразуйте её так, чтобы она выглядела как обычное предложение: "Python is a popular language". Используйте методы lower() и capitalize() (или title()).

text = "PyThOn Is A pOpUlAr LaNgUaGe"
print(text.capitalize())

#
# Задача 6 (Поиск find, count)
# Дана строка: sentence = "The quick brown fox jumps over the lazy dog"
#
# Найдите индекс первого вхождения буквы "o" (используйте find).
#
# Найдите индекс последнего вхождения буквы "o" (используйте rfind).
#
# Посчитайте, сколько раз буква "o" встречается в строке (count).

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.find('o'))
print(sentence.rfind('o'))
print(sentence.count('o'))

# Задача 7 (Проверка содержимого)
# Напишите код, который проверяет следующие строки и выводит True или False:
# Начинается ли "report_2024.pdf" с "report"?
# Заканчивается ли "image.jpeg" на ".png"?
# Состоит ли строка "12345" только из цифр?
# Состоит ли строка "Hello123" только из букв?
# Состоит ли строка " " (три пробела) только из пробельных символов?

string = 'report_2024.pdf'
print(string.startswith('report'))
string1 = 'image.jpeg'
print(string1.endswith('.png'))
string2 = '123456'
print(string2.isdigit())
string3 = 'Hello123'
print(string3.isalpha())
string4 = '   '
print(string4.isspace())

# Задача 8 (Удаление символов strip)
# Дана "грязная" строка: data = "***!!!Важное сообщение!!!***"
# Очистите её от символов * и ! с обоих концов, чтобы получить "Важное сообщение".

data = "***!!!Важное сообщение!!!***"
print(data.strip('***!!!'))

# Задача 9 (Замена replace)
# Дана строка: text = "Я люблю программировать на Java. Java - это круто."
# Замените все вхождения "Java" на "Python".

text = "Я люблю программировать на Java. Java - это круто."
print(text.replace('Java','Python'))


# Задача 10 (Разделение split)
# Дан список покупок в виде строки: items = "молоко,хлеб,яйца,масло,сыр"
# Превратите эту строку в список строк, используя метод split().
#
# Задача 11 (Склеивание join)
# Дан список слов: words = ["Python", "это", "просто", "отлично"]
# Соберите из них строку, разделив слова пробелом. Используйте join()

items = "молоко,хлеб,яйца,масло,сыр"
print(items.split(','))

words = ["Python", "это", "просто", "отлично"]
print(', '.join(words))

# Задача 12 (Индексы и срезы)
# Дана строка: alphabet = "0123456789"
# С помощью срезов получите и выведите на экран:
# Первые 5 символов ("01234")
# Последние 3 символа ("789")
# Каждый второй символ ("02468")
# Строку в обратном порядке ("9876543210")

alphabet = "0123456789"
print(alphabet[:5])
print(alphabet[-3:])
print(alphabet[::2])
print(alphabet[::-1])

# Задача 13 (in и not in)
# Дана строка: text = "user@example.com"
# Проверьте и выведите результат:
# Содержит ли строка символ "@"?
# Содержит ли строка символ "#"?
# Содержит ли строка "example"?

text = "user@example.com"
print('@' in text)
print('#' in text)
print('example' in text)


# Задача 14 (Комбинация методов)
# Дана строка: username = " AlIce In WoNdErLaNd "
# Приведите ее к "читаемому" виду: удалите лишние пробелы по краям и сделайте так, чтобы каждое слово начиналось
# с заглавной буквы (остальные — строчные). Используйте strip() и title().

# Задача 15 (Сложная замена)
# Дана строка с телефоном: phone = "+7 (999) 123-45-67"
# Используя replace() несколько раз (или цепочку вызовов), удалите все пробелы, скобки и дефисы, чтобы получить "+79991234567".

username = " AlIce In WoNdErLaNd "
username1 = username.strip().lower().title()
print(username1)

phone = "+7 (999) 123-45-67"
new_phone = (phone.replace(" ", "")
             .replace("-", "")
             .replace("(", "")
             .replace(")", ""))
print(new_phone)

# Задача 16 (f-строки)
# Создайте три переменные: product = "ноутбук", price = 75000, brand = "Lenovo".
# Используя f-строку, сформируйте предложение: "Ноутбук Lenovo стоит 75000 рублей."

product = "ноутбук"
price = 75000
brand = "Lenovo"
print(f'{product.title()} {brand} стоит {price} рублей')

# Задача 17 (f-строки с выражениями)
# У вас есть x = 12 и y = 5. С помощью одной f-строки выведите: "12 + 5 = 17", "12 - 5 = 7", "12 * 5 = 60".

x = 12
y = 5
print(f'{x} + {y} = {x + y}')