# Перебор словоря в цикле

student = {
    'name':'Sergei',
    'surname':'Kochkin',
    'age':30,
    'is_married':True,
}

# Перебор ключей

# .keys() -> dict_keys()
print(student.keys())

# для работы с dict_keys() как со спискомнужно использовать функцию list()
dict_keys_list = list(student.keys())
print(dict_keys_list)

for key in student.keys():
    print(key)
    print(f'{key}: {student[key]}')

# for key in dict -> предпочтительный метод
for k in student:
    print(k)
    print(f'{k} = {student[k]}')

# Перебор значений
# values()

values = student.values()
print(values)
values_list = list(student.values())
print(values_list)

for v in student.values():
    print(v)

grades = {
    'Math':5,
    'English':4,
    'Art':5,
    'Chemistry':4,
}

for grad in grades.values():
    print(grad)

# средняя оценка = сумма / количество
# sum() - получение суммы

grades_sum = sum(grades.values())
print(grades_sum)
grades_count = len(grades.values())
print(grades_count)
average_grade = grades_sum / grades_count
print(average_grade)

# Перебор пар ключ значения

# items() -> dict_items()
print(student.items())

for k,v in student.items():
    print(f'{k}: {v}')

# Пример 1: Поиск максимального значения
scores = {
    'Анна': 85,
    'Борис': 92,
    'Вика': 78,
    'Глеб': 88
}
max_score_student_name = None
max_score = None

for student_name,score in scores.items():
    if max_score is None or score > max_score:
        max_score_student_name = student_name
        max_score = score

print(max_score_student_name)
print(max_score)

# Пример 2: Создание нового словаря с условием

grades = {
        'Математика': 5,
        'Физика': 3,
        'Русский': 4,
        'Химия': 2,
        'Литература': 1,
        'Английский': 3,
}

good_grades = {}

for subject, grade in grades.items():
    if grade >= 4:
        good_grades[subject] = grade
print(good_grades)

# Пример 3: Подсчет частоты символов

text = "hello world"
char_count = {}

for cher in text:
    char_count[cher] = char_count.get(cher, 0) + 1

for cher, count in char_count.items():
    print(f'{cher} = {count}')


#  Изменение словаря во время перебора
# ⚠️ Осторожно! Нельзя удалять элементы при переборе:
#
# ❌ Ошибка!
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     if key == 'b':
#         del d[key]  # RuntimeError: dictionary changed size during iteration

# Словарные включения (dict comprehension)

prices = {'яблоко': 100, 'банан': 80, 'апельсин': 120}
new_prices ={}
for product, price in prices.items():
    new_prices[product] = int(price * 1.1)
print(new_prices)

upgraded_prices = {product:int(price*1.1) for product, price in prices.items()}
print(upgraded_prices)

# Оставить только товары дороже 100
products = {
    'мышь': 500,
    'коврик': 300,
    'карандаш': 50,
    'блокнот': 80
}
expensive_products = {product: price for product, price in products.items() if price > 100}
print(expensive_products)