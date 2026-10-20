# Хранение типов данных в памяти

# Все типы данных в Python являются объектами

# str
name = 'Sergei'
# обращение к значению переменной
print(name)
# взятие типа переменной
print(type(name))
# id(name) - адрес памяти
print(id(name))

name_copy = name
print(id(name_copy))

name= 'Sergei Kochkin'
print(name)
print(id(name))

print(name_copy)
print(id(name_copy))


numbers = [1,2,3,4,5]
numbers_copy = numbers

print(numbers)
print(id(numbers))
print(numbers_copy)
print(id(numbers_copy))

numbers.append(6)
print(numbers)
print(id(numbers))
print(numbers_copy)
print(id(numbers_copy))

numbers.clear()
print(numbers)
print(id(numbers))
print(numbers_copy)
print(id(numbers_copy))

a=4
b=[4]
result=(a,b)
print(result)   # (4, [4])
a=5
b.append(5)
print(result)   # ?

num_1 = 100
print(id(num_1))
num_2 = num_1
print(id(num_2))

num_1 = 999
print(num_1)
print(id(num_1))
print(num_2)
print(id(num_2))

course = {
    'title':'python',
    'duration': 6,
    'price': 50_000.25,
    'is_completed': False
}

course_clone = course
course_copy =course_clone
course['teacher'] = 'Vadim'
print(course)
print(course_clone)
print(course_copy)

list = [1,2,3,4,5]
list_copy=list
print(list)
print(list_copy)
list_copy.append(6)
print(list)
print(list_copy)

list_copy.clear()
print(list)
print(list_copy)

number_1 = 1111
number_2 = number_1
number_1 = 0
print(number_1)
print(number_2)


