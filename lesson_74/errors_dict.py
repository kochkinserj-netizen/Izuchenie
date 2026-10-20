# Частые ошибки при работе со словорями




# Ошибка 1: Изменение словаря во время перебора

# ❌ ОШИБКА!
grades = {
    'Анна': 5,
    'Борис': 3,
    'Вика': 4,
    'Глеб': 2
}
# RuntimeError: dictionary changed size during iteration
# for student in grades:
#     if grades[student] < 3:
#         del grades[student]

# Правильные решения
# ✅ Решение 1: Создать список ключей для перебора
grades = {'Анна': 5, 'Борис': 3, 'Вика': 4, 'Глеб': 2}

for student in list(grades.keys()):  # list() создает копию ключей
    if grades[student] < 3:
        del grades[student]

print(grades)  # {'Анна': 5, 'Вика': 4}

# ✅ Решение 2: Создать новый словарь
grades = {'Анна': 5, 'Борис': 3, 'Вика': 4, 'Глеб': 2}
new_grades = {}

for student, grade in grades.items():
    if grade >= 3:
        new_grades[student] = grade

print(new_grades)  # {'Анна': 5, 'Вика': 4}



# Ошибка 2: Неправильная проверка наличия ключа

# ❌ ОШИБКА!
student = {'name': 'Анна', 'age': 20}
#
# if student['grade'] > 80:  # KeyError: 'grade'
#     print("Отлично!")

# ✅ Решение 1: Проверка через in
if 'grade' in student:
    if student['grade'] > 80:
        print("Отлично!")
else:
    print("Оценка отсутствует")

# ✅ Решение 2: Использование get()
grade = student.get('grade', 0)  # 0 - значение по умолчанию
if grade > 80:
    print("Отлично!")

# ✅ Решение 3: Проверка на None
if student.get('grade') is not None:
    print(f"Оценка: {student['grade']}")


# Ошибка 3: Путаница между .get() и []

# Разница между [] и .get()

student = {'name': 'Анна'}

# [] - вызывает ошибку при отсутствии ключа
# print(student['age'])     # KeyError

# .get() - возвращает None (или значение по умолчанию)
print(student.get('age'))  # None
print(student.get('age', 0))  # 0

# ❌ ОШИБКА: Использование .get() для присваивания
#student.get('age') = 20  # SyntaxError: нельзя присвоить вызову функции

# ✅ Правильно: используйте [] для присваивания
# student['age'] = 20

# ❌ ОШИБКА: Предположение, что .get() всегда вернет значение
# if student.get('grade') > 80:  # TypeError, если grade нет (None > 80?)
#     print("Отлично!")
# Правильное использование
# ✅ Для чтения с значением по умолчанию
grade = student.get('grade', 0)

# ✅ Для проверки существования
if student.get('grade') is not None:
    print(student['grade'])

# ✅ Для присваивания только с []
student['grade'] = 90



# Ошибка 4: Изменение словаря при использовании .items()

# ❌ ОШИБКА!
prices = {'яблоко': 100, 'банан': 80, 'апельсин': 120}

for product, price in prices.items():
    if price < 100:
        prices[product] = price * 1.1  # Можно изменять значение
        # Но добавлять/удалять элементы НЕЛЬЗЯ!
        prices['виноград'] = 150  # RuntimeError!
# Правильное решение
# ✅ Если нужно добавить новые ключи - создайте копию
prices = {'яблоко': 100, 'банан': 80, 'апельсин': 120}
new_prices = prices.copy()

for product, price in prices.items():
    if price < 100:
        new_prices[product] = price * 1.1

new_prices['виноград'] = 150
print(new_prices)

# Ошибка 5: Неправильное копирование словарей
original = {'a': [1, 2, 3], 'b': {'c': 4}}

# ❌ ОШИБКА: Простое присваивание
copy1 = original  # Это не копия! Это ссылка на тот же словарь
copy1['a'][0] = 999
print(original['a'])  # [999, 2, 3] - изменился оригинал!

# ⚠️ Поверхностная копия
copy2 = original.copy()  # или dict(original)
copy2['a'][0] = 777
print(original['a'])  # [777, 2, 3] - все еще изменился!

# ✅ Для глубоких копий (для вложенных структур) нужно использовать пакет copy, с которым мы познакомимся в будущем
import copy
copy3 = copy.deepcopy(original)
copy3['a'][0] = 555
print(original['a'])  # [777, 2, 3] - НЕ изменился!
print(copy3['a'])     # [555, 2, 3]
# Когда нужна глубокая копия?
# Простые словари (без вложенностей) - copy() достаточно
simple = {'a': 1, 'b': 2}
copy_simple = simple.copy()
copy_simple['a'] = 100
print(simple['a'])  # 1 (не изменился)

# Сложные (списки, словари внутри) - нужна deepcopy()
complex_dict = {'list': [1, 2, 3], 'dict': {'x': 10}}
copy_complex = complex_dict.copy()
copy_complex['list'][0] = 999  # Изменит оригинал!
# Ошибка 6: Использование изменяемых объектов как ключей
# ❌ ОШИБКА! Список - изменяемый тип
d = {}
key = [1, 2, 3]
d[key] = 'value'  # TypeError: unhashable type: 'list'

# ❌ Словарь тоже нельзя использовать как ключ
d = {}
key = {'a': 1}
d[key] = 'value'  # TypeError: unhashable type: 'dict'

# ✅ Только неизменяемые типы: строки, числа, кортежи (если внутри неизменяемые)
good_dict = {
    'name': 'Анна',      # строка
    42: 'answer',        # число
    (1, 2): 'point'      # кортеж из чисел
}

# ⚠️ Кортеж со списком внутри - тоже изменяемый
bad_key = (1, [2, 3])  # TypeError при использовании как ключа
# Почему это важно?
# Ключи словаря должны быть хешируемыми (неизменяемыми). Изменяемые объекты нельзя использовать, потому что если изменить ключ, словарь потеряет возможность найти значение.

# Ошибка 7: Путаница с методами keys(), values(), items()
data = {'a': 1, 'b': 2, 'c': 3}

# ❌ ОШИБКА: Думать, что keys() возвращает список
keys = data.keys()
keys[0]  # TypeError: 'dict_keys' object is not subscriptable

# ✅ Преобразуйте в список, если нужен индекс
keys_list = list(data.keys())
print(keys_list[0])  # 'a'

# ❌ ОШИБКА: Изменение словаря через views
views = data.keys()
data['d'] = 4  # view автоматически обновляется
print(views)   # dict_keys(['a', 'b', 'c', 'd'])

# ⚠️ Но нельзя изменять словарь во время итерации по view
for key in data.keys():
    if key == 'b':
        data['e'] = 5  # RuntimeError!
# Правильное использование
# ✅ Для перебора - можно ключей dict
for key in data:
    print(key)

# ✅ Для получения списка - используйте list()
keys_list = list(data.keys())

# ✅ Для проверки - можно использовать in напрямую
if 'a' in data:  # быстрее, чем 'a' in data.keys()
    print("Есть")
# Ошибка 8: Неправильное удаление элементов
student = {'name': 'Анна', 'age': 20, 'grade': 5}

# ❌ ОШИБКА: Удаление без проверки
del student['address']  # KeyError: 'address'

# ✅ Правильно: сначала проверять
if 'address' in student:
    del student['address']

# ✅ Или использовать pop() с возвратом значения
removed = student.pop('address', None)  # не вызовет ошибку
print(removed)  # None

# ⚠️ pop() без значения по умолчанию вызовет ошибку
removed = student.pop('address')  # KeyError!

# ✅ popitem() удаляет последний элемент
last_item = student.popitem()  # ('grade', 5)
print(student)  # {'name': 'Анна', 'age': 20}
# Сравнение методов удаления
# del - просто удаляет (быстро, но нет возврата)
if key in dict:
    del dict[key]

# pop - удаляет и возвращает значение
# value = dict.pop(key, default)

# popitem - удаляет и возвращает последнюю пару
key, value = dict.popitem()

# clear - удаляет все
dict.clear()
# Ошибка 9: Ожидание порядка элементов
# До Python 3.7 словари НЕ сохраняли порядок!
# ❌ ОШИБКА: Рассчитывать на порядок в старых версиях

# Даже в Python 3.7+ порядок сохраняется, но не стоит на него полагаться
d = {'a': 1, 'b': 2, 'c': 3}

# ✅ Для гарантированного порядка используйте список ключей
ordered_keys = ['a', 'b', 'c']
for key in ordered_keys:
    print(d[key])

# ✅ Или используйте collections.OrderedDict
from collections import OrderedDict
ordered = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# Ошибка 10: Неправильное использование словаря для подсчета
# ❌ ПЛОХО: Много проверок
words = ['a', 'b', 'a', 'c', 'b', 'a']
count = {}

for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

# ✅ ЛУЧШЕ: Использовать get()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
# Ошибка 11: Неэффективные операции
# ❌ МЕДЛЕННО: Двойной поиск
if key in dict:
    value = dict[key]  # второй поиск

# ✅ БЫСТРО: Один поиск
value = dict.get(key)
if value is not None:
    print(value)


# ❌ МЕДЛЕННО: Создание списка ключей для проверки
if key in list(dict.keys()):  # создает список всех ключей
    print(dict[key])

# ✅ БЫСТРО: Прямая проверка
if key in dict:
    print(key)