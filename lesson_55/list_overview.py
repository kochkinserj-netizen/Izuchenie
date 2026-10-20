# Практика работы со списками

# Списки имеют такие характеристики
# изменяемые
# индексируемые
# могут хранить разные типы

countries = ['UK', 'Japan', 'China', 'New Zealand', 'Austria']
ids = [0,1,2,3,4,5]
users = [
    {
        'id':0,
     'name': 'Gorg'
     },
    {
        'id':1,
     'name': 'Jon'
     }
]

countries.append('Germany')
print(countries)

countries[2] = 'Russia'
print(countries)

# Доступ к элементам списка
# нумерация начинается с 0
# последний элемент -1
# len(list) - 1

print(len(countries))

# Срезы
# list[start:finish:step]
# Поворот списка -> list[::-1]
print(countries[-2:])
print(countries[::-1])

# Добавление в список

# append() - добавление в конец
countries.append('France')
print(countries)

# insert() - Вставка по индексу
countries.insert(0,'Spanish')
print(countries)

# extend() - добавление списка в споисок
nordic_countries = ['Finland', 'Sweden', 'Switzerland']
countries.extend(nordic_countries)
print(countries)

eropean_countries = ['poland', 'ukraine', 'belarus']
eropean_countries2 = nordic_countries + eropean_countries
print(eropean_countries2)
print(nordic_countries)

# Удаление по значению

# remove() - Удалить по значению
country = 'India'
if country in countries:
    countries.remove(country)
else:
    print(f'{country} is not in the list')

# pop() - Удалени по индексу
country_index = 33
if country_index in countries:
    countries.pop(country_index)
else:
    print(f'Index {country_index} is not in the list')

# clear() - Очистить список
african_countries = ['Kongo', 'Aljhir', 'SAR']
print(african_countries)
african_countries.clear()
print(african_countries)

# count() - Сколько раз встречается
print(countries)
print(countries.count(country))

# index() - Поиск по значению
# print(countries.index(country))  неправельный поиск

if country in countries:
    print(countries.index(country))
else:
    print(f'{country} is not in the list')

# sort() - сортировка на месте
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True) # сортировка в обратном порядке
print(countries)

# copy() - создание копии
countries_copy = countries.copy()

# sorted() - сортировка с возвращением результата в новы список
sorted_countries = sorted(countries)
print(sorted_countries)
print(countries_copy)
print(countries)

# reverse() - разворачивает список на месте

countries.reverse()
print(countries)

# Как развернуть список без изменения исходного
reversed_countries =sorted_countries[::-1]
print(reversed_countries)

# Копирование списка
countries_twins = countries
print(countries_twins)
print(countries)
countries.append('Portugal')
# == оператор проверки по значению
print(countries_twins == countries)

# is оператор проверки индентичности, те переменные ссылаются на одно и то же значение в памяти
print(countries_twins is countries)
