# Изменяемые и неизменяемые типы данных

# Изменяемые тиипы (mutable) это данные, содержимое можно менять после создания

# К изменяемым относятся
# - list
# - dict
# - set
# - bytearray


# list

students = ['John','Michael','David']
print(students)
print(type(students))
# .append Метод добавления в конец списка
students.append('Vadim')
print(students)
#  .insert метод добавления по порядковому номеру
students.insert(1,'Peter')
print(students)
# .clear() Метод очистки списка
students.clear()
print(students)

# dict
user= {
    'name':'Sergei',
    'surname':'Kochkin',
    'age': 30,
    'city': 'Kirov',
    'company':'Avitech',
    'salary': 200_000
}
print(user)
print(type(user))

# dict['new_property'] - установка нового значения
user['is_married'] = True
print(user)
print(type(user))

# dict['exist_property'] - установка нового значения
user['city'] = 'Vladivostok'
print(user)

# .clean() - очистка словоря
user.clear()
print(user)

# set
students_names ={'Max', 'Alex', 'Andrew', 'Oleg', 'Andrew', 'Anna'}
print(students_names)
print(type(students_names))
# .add - добавление в список
students_names.add('Sergei')
print(students_names)
# .remove - добавление элемента во множество
students_names.remove('Max')
print(students_names)

# immutable
#  str
full_name = 'Sergei Kochkin'
full_name.upper()
print(full_name)
full_name_upper = full_name.upper()
print(full_name)
print(full_name_upper)

#  tuple
tols = ('Python','Java','C++')
print(tols)
# у кортеже нет метода на модификацию данных

#  frozenset
fr = frozenset([1,2,3])
#  frozenset не содержит методов на модтфикацию