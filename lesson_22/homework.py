
# 1. Преобразование строки в верхний регистр
text = "hello world"
print(text.upper())
# HELLO WORLD

# 2. Преобразование строки в нижний регистр
text = "HELLO PYTHON"
print(text.lower())
# hello python

# 3. Сделать первую буква заглавной
text = "hello world"
print(text.capitalize())
# Hello world

# 4. Сделать каждое слово с заглавной буквы
text = "hello python world"
print(text.title())
# Hello Python World

# 5. Поменять регистр на противоположный
text = "Hello Python"
print(text.swapcase())
# hELLO pYTHON

# 6. Найти индекс подстроки world безопасно
text = "hello world"
print(text.find('world'))
# 6

# 7. Найти индекс подстроки hello с конца безопасно
text = "hello world hello"
print(text.rfind('hello'))
# 12

# 8. Поиск индекса небезопасно подстроки programming
text = "python programming"
print(text.index('programming'))
# 7

# 9. Сделать подсчет вхождений буквы a
text = "banana"
print(text.count('a'))
# 3

# 10. Проверить что строка начинается на подстроку hello
text = "hello world"
print(text.startswith('hello'))
# True

# 11. Проверить что строка заканчивается на подстроку .pdf
text = "resume.pdf"
print(text.endswith('.pdf'))
# True

# 12. Проверить что строка состоит только из букв
text = "Hello"
print(text.isalpha())
# True

# 13. Проверить что строка состоит только из цифр
text = "12345"
print(text.isdigit())
# True

# 14. Проверить что строка состоит только из букв и/или цифр
text = "Hello123"
print(text.isalnum())
# True

# 15. Проверить что строка состоит только из пробелов
text = "   "
print(text.isspace())
# True

# 16. Замена Java на Python
text = "I like Java"
print(text.replace("Java", "Python"))
# I like Python

# 17. Удаление пробелов с обеих сторон
text = "   hello world   "
print(text.strip())
# hello world

# 18. Удаление пробелов слева
text = "   hello"
print(text.lstrip())
# hello

# 19. Удаление пробелов справа
text = "hello   "
print(text.rstrip())
# hello

# 20. Сделать из строки список фруктов
text = "apple,banana,orange"
print(text.split(','))
# ['apple', 'banana', 'orange']

# 21. Сделать из списка строку
words = ["Python", "is", "awesome"]
print(' '.join(words))
# Python is awesome

# 22. Все символы строки заглавные буквы
text = "HELLO"
print(text.isupper())
# True

# 23. Все символы строки строчные буквы
text = "hello"
print(text.islower())
# True

# 24. Каждое слово начинается на заглавную буквы
text = "Hello World"
print(text.istitle())
# True

# 25. Замена первое 1 яблоко на апельсин, а второе на лимон
text = "apple apple apple"
new_text = (text
            .replace("apple", "orange",1)
            .replace("apple", "lemon",1))
print(new_text)
# orange lemon apple

# 26. Разбить строку на список из трёх элементов
text = "one two three four"
print(text.split())
# ['one', 'two', 'three four']

# 27. Привести строку к списку *
text = "apple, banana; orange. peach"
new_text = ((text
            .replace(',',''))
            .replace(';','')
            .replace('.',''))
print(new_text.split())
# ['apple', ' banana', ' orange', peach]

# 28. Сделать строку даты в формате YYYY-MM-DD
words = ["2024", "01", "15"]
print('-'.join(words))
# 2024-01-15

# 29. Проверить, содержится ли подстрока вадим в тексте без учёта регистра
text = 'Школа Вадима Звягинцева'
print('вадим' in text.lower())
# True
