# Методы списков

countries = []
# 1. Добавление в спиок

# append(value) - добавление элемента в  конец списка
countries.append('Russia')
print(countries)
countries.append('Finland')
countries.append('Poland')
#countries.append('uk','usa') - можно добавить только один элемент

print(countries)

# insert(index,value) - добавление по индексу нового элемента ( незаменяет)
countries.insert(0, 'France')
print(countries)
countries.insert(0, 'Germany')
print(countries)
countries.insert(4, 'Spain')
print(countries)

# extend(iterable) - добовляет список в конец списка
asian_countries = ['China', 'Thailand', 'Japan']
world_countries = countries + asian_countries
print(world_countries)

european_countries = countries.copy()
european_countries.extend(asian_countries)
print(countries)
print(european_countries)

# 2. Удаление элементов

# remove(value) - удаление по значению
# если значения нет в списке то будет ValueError
# Для предотвращения ошибки используем операторы in/not in

france = 'France'
if france in countries:
    countries.remove(france)

print(countries)

# pop(index) - удаление по индексу
# если индекса нет то удаляется последний элемент списка
# если индекс не в диапазоне -> IndexError

germany = 'Germany'
# germany_index = -1
germany_index = None

if germany in countries:
    germany_index = countries.index(germany)

print(germany_index)

# if germany_index >=0:
if germany_index is not None:
    countries.pop(germany_index)
print(countries)

# clear() - очистка списка -> сделать список пустым []
european_countries.clear()

# index(value) - поиск элемента по значению и возврат его индекса
# если значения нет то -> ValueError
# метод небезопасный

australia = 'Australia'
if australia in countries:
    print(countries.index(australia))


# count(value) - количество повторений
# если значений нет то будет ноль повторений
print(countries.count('Australia'))

# sort()- сортировка на месте
countries.sort()  # сортировка на месте
print(countries)
countries.sort(reverse=True)  # Сортировка в обратном порядке
print(countries)

# revers() - разворот списка, без сортировки

