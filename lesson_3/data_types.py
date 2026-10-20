# Типа данных в Python

# Числовые типы numeric data types


# int- целые
age = 30
print(age)
print(type(age)) # как узнать тип данных

temperature = -16

zero = 0

big_number = 544545515687961312164


# float - числа с ТОЧКОЙ
body_temperature =36.6
print(body_temperature)
print(type(body_temperature))

winter_temperature = -16.5
print(winter_temperature)

small_number = 0.000000015
print(small_number)

a=0.1
b=0.2
c=a+b
print(c) #  = 0.30000000000000004  Особенность плавующей точки связанное с потерей точности


# Complex- комплексные числа
c1 = 1 + 2j
c2 = -3.5 + 4.5j

# Строки (Strings)  str
# str - всегда в ковычках, не важно в каких
name = 'Sergei'
print(name)
print(type(name))

surname = 'Vladimirovich'
print(surname)
print(type(surname))

phone_number = '+1 234 567 890'
print(phone_number)
print(type(phone_number))
# числа можно далать строкой спомощью ковычек
# ковычки должны быть одинаковые с двух сторон


# bool - булево значение, логический тип, переменные объявляются с is
# их всего два типа True, False

is_russian= True
print(is_russian)
print(type(is_russian))

is_married = False
print(is_married)
print(type(is_married))

# Отсутствие значения None

teacher= None
print(teacher)
print(type(teacher))



# Коллекции(структуры данных)

#list- список. Упорядоченная изменяемая коллекция элементов.
programming_languages = ['Python', 'Java', 'Ruby', 'PHP']
print(programming_languages)
print(type(programming_languages))

empty_list = [] # списки могут быть пустыми
print(empty_list)
print(type(empty_list))

diff_types_list = ['Sergei', 'Vladimirovich', 36.6, 30] #списки могут быть из из разных типов данных
print(diff_types_list)

# tuple — кортеж. Упорядоченная неизменяемая коллекция элементов.
student_name = ('Anatolii','Boris','Valera')
print(student_name)
print(type(student_name))

# set - Множество. нет дубликатов, нет порядка
cities = {'San Francisco','Moscow','New York','San Francisco'}
print(cities)
print(type(cities))

# dict - словарь в формате ключ-значение правила JOIN
users = {
        'Anatolii':'Teacher',
        'Boris':'Student',
        'age':23,
        'is_married':True,
        'friends':['Mike','Jonn']}
print(users)
print(type(users))


# range деопазон
numbers= range(1,32)
print(numbers)
print(type(numbers))

#frozenset
fz=frozenset([1,4454,25.5])
print(fz)
print(type(fz))
"""
Примитивы
NoneType
Списки
Специальные типы данных
"""


