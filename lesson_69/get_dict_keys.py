# Доступ к элементам словаря

laborer = {
    'id':1,
    'name':'Sergei',
    'surname':'Kochkin',
    'age': 30,
    'company': 'Big',
    'title':'Python Developer',
    'salary': 500_000,
    (1,2): 123
}
# доступ по ключу (небезопасен)
print(laborer['name'])
print(laborer['salary'])
# print(laborer['city']) при обращению по несуществующему ключу, будет ошибка

# проверка наличия ключа через оператор in
key = 'city'
if key in laborer:
    print(laborer[key])
else:
    print(f'Key \'{key}\' not found in laborer')

# Метод get() — безопасный доступ
print(laborer.get('city')) # если ключа нет то получаем None
print(laborer.get('title'))

# второй аргумент это значение по умолчанию, если нет ключа то вызывается второе значение
print(laborer.get('country', 'Russia'))
print(laborer.get((1,2)))

# изменение значения по прямому доступу через ключ
laborer['salary'] = 550_000
print(laborer['salary'])


# при присваивание значения словарю, проверяется есть ли ключ в словаре:
# если он есть ,то значение перезаписывается
# если ключа нет, то в словарь добавляется новый ключ с преданым значением

laborer['city'] = 'Moscow'
print(laborer['city'])

print(len(laborer)) # длинна словаря -> количество пар ключ:значение
