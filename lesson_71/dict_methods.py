# Методы словарей

new_dict =dict()
new_dictionary = {}

teacher = {
    'name':'Vadim',
    'surname':'Zviagintsev',
    'age':21,
    'is_married':True,
    'company':'Big Tech',
    'title':'Python Developer',
    'salary':500_000,
    'friend':['Jonn','Kevin']
}

# keys() - метод возвращения ключей словаря
# dict_keys - подобная списку структура ключей
keys = teacher.keys()

print(keys)
print(type(keys))

# dict_keys можно преобразовать в обычный лист
lst = list(keys)
print(lst)

for key in keys:
    print(key)
    print(teacher[key])

# values() - возвращает все значения словаря в dict_values
values = teacher.values()
print(values)

teacher['city'] = 'Moscow'

# после монипуляций с данными в словаре dict_keys, dict_values автоматически подтягивается ключи и значения
print(values)
print(keys)
# в спеиске хронятся значения которые были на момент создания этого списка
print(lst)  # -> здесь не будет teacher['city'] = 'Moscow'

# items() - возвращение пар ключ значений в виде кортежей dict_items

items = teacher.items()
print(items)

# update() - добовляет новые пары в исходный словарь
# можно объеденять словари
print(len(new_dict))
# id, name, surname, city, occupation
new_dict['id'] = 324
new_dict['name'] = 'Vadim'
new_dict['surname'] = 'Zviagintsev'
new_dict['city'] = 'Moscow'
new_dict['occupation'] = 'Python Developer'
print(new_dict)

print(len(new_dictionary))
new_dictionary.update({
    'state':'NY',
    'salary':520_000,
    'is_maried':False
})
print(new_dictionary)

new_dict.update(new_dictionary)
print(new_dict)
# при объеденении, одинаковый ключ будет перезаписан

# copy() - копия словаря
# Метод copy() создаёт поверхностную копию словаря:
teacher_bpother = teacher
teacher_copy = teacher.copy()

print(id(teacher_copy))
print(id(teacher_bpother))
print(id(teacher))

print(id(teacher_copy['friend']))
print(id(teacher['friend']))

teacher_copy['friend'].append('Billi')
print(teacher_copy)
print(teacher_bpother)
print(teacher)


# setdefault - если ключ есть то значение не меняется , если ключа нет то он его устанавливает
# так же возвращает значение по ключу

student ={
    'id':123,
    'name':'Vadim',
    'surname':'Zviagintsev',
    'course':'Python'
}

student['course'] = 'JS'
print(student['course'])

student.setdefault('age',23)
print(student)

student.setdefault('course','Python')
print(student)

# fromkeys(iterable,default) - создание словаря из ключей

keys = ['id', 'name', 'surname', 'age', 'course']

# dict_draft = {}.fromkeys(keys)
dict_draft = dict.fromkeys(keys, '')

print(dict_draft)

