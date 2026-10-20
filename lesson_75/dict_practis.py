# Практичаска работа со словорями

grades = {
    'Анна':     [5, 4, 5, 5, 4],
    'Борис':    [3, 4, 3, 4, 3],
    'Вика':     [5, 5, 5, 4, 5],
    'Глеб':     [2, 3, 3, 4, 3]
}

# Вывести всех учиников и их средний бал

for key, value in grades.items():
    avg = sum(value) / len(value)
    print(f'{key}: {avg}')

print('---'*50)

# вывести отличников (средний бал >= 4.5)

for name, grade in grades.items():
    avg = sum(grade) / len(grade)
    if avg >= 4.5:
        print(name)

print('---'*50)

# Наити двоечника

for name, grade in grades.items():
    if 2 in grade:
        print(name)

print('---'*50)
print('---'*50)

# Телефонная книга: имя → номер
phone_book = {
    'Анна': '+7-123-456-7890',
    'Борис': '+7-234-567-8901',
    'Вика': '+7-345-678-9012',
    'Дима': '+7-456-789-0123'
}

# поиск номера по имени
searched_name = 'Борис'
for name, phone in phone_book.items():
    if name in searched_name:
        print(phone)
else:
        print(f'Имя {searched_name} отсутствует в книге')

if searched_name in phone_book:
        print(phone_book[searched_name])
else:
        print(f'Имя {searched_name} отсутствует в книге')


print('---'*50)

# Показать все контакты

for name,phone in phone_book.items():
    print(f'{name}: {phone}')

print('---'*50)

# Добавление нового клиента
new_client = ('Сергей')
new_phone = '+7-123-456-7890'
phone_book[new_client] = new_phone

print(phone_book)

print('---'*50)

# Удаление клиента

delited_name = ("'Дима'")
if delited_name in phone_book:
    del phone_book[delited_name]
    print(f'Пользователь {delited_name} удален')
else:
    print(f'Пользователь {delited_name} не найден в телефонной книге')

print('---'*50)
print('---'*50)

text = "кот собака кот кот рыба кот собака рыба рыба кот слово слово клон трон кудяплик кудяплик"

# Разбиваем текст на слова

# перевод строки в список

words = text.split()
print(words)
print('---'*50)
# создание словаря с количеством повторения слова
words_dict = {}
for w in words:
    if w not in words_dict:
        words_dict[w] = 1
    elif w in words_dict:
        words_dict[w] += 1

print(words_dict)
print('---'*50)
# Отображение слова и количества повторений
for word, count in words_dict.items():
    print(f'{word}: {count}')


print('---'*50)

#  Самое частое слово

for word, count in words_dict.items():
    if count == max(words_dict.values()):
        print(f'{word}: {count}')

print('---'*50)
print('---'*50)

# Цены товаров
prices = {
    'хлеб': 50,
    'молоко': 80,
    'яйца': 100,
    'масло': 150,
    'сыр': 200
}

# Корзина покупателя: товар → количество
cart = {
    'хлеб': 2,
    'молоко': 1,
    'сыр': 1
}

# Подчет стоимости корзины
total_price = 0
for product, count in cart.items():
       if product in prices:
           product_price = prices[product] * count
           total_price += product_price

print(f'Итого: {total_price}')

print('---'*50)

# Добавление товара в корзину

product = 'сыр'
count_product = 4
if product not in cart:
    cart[product] = count_product
else:
    cart[product] = cart[product] + count_product
print(cart)

# проверка доступности товара

searched_product = 'масло'
if searched_product in prices:
    print(f'{searched_product.title()} стоит {prices[searched_product]}')
else:
    print(f'{searched_product.title()} отсутствует в магазине')

print('---'*50)
print('---'*50)

# Библиотека: книга → статус (True - свободна, False - выдана)
library = {
    'Война и мир': True,
    'Преступление и наказание': True,
    'Мастер и Маргарита': False,
    'Анна Каренина': True,
    'Евгений Онегин': False
}

# 1. Показать все доступные книги
for book, availability in library.items():
    if availability:
        print(book)

# 2. Выдать книгу читателю
book_name = 'Война и мир'
if book_name in library:
    if library[book_name] == True:
        library[book_name] = False
        print(f"Книга '{book_name}' выдана")
    else:
        print(f"Книга '{book_name}' уже выдана")
else:
    print(f"Книги '{book_name}' нет в библиотеке")

    
# 3. Вернуть книгу
return_book = 'Мастер и Маргарита'
if return_book in library:
    if library[return_book] == False:
        library[return_book] = True
        print(f"Книга '{return_book}' возвращена")
    else:
        print(f"Книга '{return_book}' уже в библиотеке")


# 4. Показать актуальный статус
