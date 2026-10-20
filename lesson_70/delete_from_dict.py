# Удаление элементов из словаря

user = {
    'id':1,
    'name': 'Sergei',
    'surname': 'Kochkin',
    'is_married':True,
}

print(len(user))

# clear()- полная очитска словаря
# user.clear()
print(user)

# pop(key) - небезопасное удаление по ключу
# метод возвращает значение соответствуещее ключу

user.pop('id')
print(user)

is_married = user.pop('is_married')
print(is_married)
print(user)

#user.pop('city') #KeyError: 'city'
# для удаления нужно использовать ветвление -> безопасно

key = 'city'
if key in user:
    user.pop(key)
else:
    print(f'"{key}" is not in user')

# так же для удаления можно ипользовать дефолтное значение -> безопасно
res = user.pop('city','Key not found')
print(res)


student = {
    'id':1,
    'name': 'Sergei',
    'surname': 'Kochkin',
    'is_married':True,
    'course': 'Python',
}
print(student)

# popitem() - удаление последне добавленную пару ключ:значение
last_item = student.popitem()
print(last_item)
print(type(last_item))
print(student)

item = student.popitem()
print(item)
print(student)

student.popitem()
print(student)
student.popitem()
print(student)
student.popitem()
print(student)

# при попытке выцзвать метод popitem() для пустого словаря то будет ошибка KeyError
# необходимо использовать ветвление
# student.popitem()
# print(student)

empty_dict = {}
if len(empty_dict)>0:
    empty_dict.popitem()
else:
    print('empty dict')

# del оператор удаления, небезопасное

country = {
    'name':'USA',
    'capital':'Washington',
    'president':'George Busch'
}

del country['president']
print(country)

population_key = 'population'
if population_key in country:
    del country[population_key]
else:
    print(f'"{population_key}" is not in country')