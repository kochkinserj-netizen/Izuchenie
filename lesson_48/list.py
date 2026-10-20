# Знакомство со списками (list)

numbers = [1,2,3,4,5,6,7,]
print(type(numbers))
print(numbers)
# Списки можно создавать из разных типов данных
students = ['Nick', 'David', 'John', 'Mary', 'Kevin', 'David']
print(students)
print(type(students))
print(students)

mix_list = [1, True, 'John']
print(mix_list)

# Список может состоять из вложенных списков
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

products = [
    {'id':12,'title':'Basket','price':125},
    {'id':13,'title':'Plate','price':79.54}
]

# Создание списков
# Литерал
countries = ['USA', 'UK', 'Canada']

# Через функцию list()
nums = list((1,2,3,4,5,6,7,))
print(nums)
# из set
list_from_set = list({1,2,3})
print(list_from_set)

# Создание списка из строки
name_letters = list('Sergo')
print(name_letters)

# Индексация

names = ['John', 'David', 'Kevin', 'David','Nick', 'Graham',]
# функция len() - взятие длинны
print(len(names))
# индексы начинаются с нуля

# Обращение по индексу внутри списка
print(names[0])
# При обращенни по несуществующему идексу вызовет ошибку

# Срезы
# [start;end;step]

name_copy = names[:]
print(name_copy)

names_slice1 = names[2:]
print(names_slice1)

names_slice2 = names[:2]
print(names_slice2)
# Реверс списка
names_reverse = names[::-1]
print(names_reverse)

# Изменение элементов
# список можем менять по индексу
names[0] = 'Sergei'
print(names)

print(len(names))
# Проверка на наличее в списках
print('Sergei' in names)
if 'Sergei' in names:
    print('Sergei is Python automation student')

# Конкатенация списков
automation_backend = ['Vito', 'Frank', 'Lari']
automation_frontend = ['Oliver', 'Nick']

python_automation = automation_backend + automation_frontend
print(python_automation)

# Повторение списков
lang = ['Python', 'Java', 'C++', 'JavaScript']
print(lang*3)

# Методы списка
new_list = []
# new_list[0] = 'Python'
# print(new_list)

# append(value) - Добавление в список в конец ОДНОГО значения
new_list.append('Sergei')
print(new_list)
new_list.append('Lari')
print(new_list)

# extend(iterable) - добавления одного списка в другой списо в конец
automation_frontend.extend(automation_backend)
print(automation_frontend)

new_list.extend(['Mick', 'Mike'])
print(new_list)

# insert(index,value) - вставляет по указанному идексу переданное значение (лучше использовать для вставки в начало или середину)
new_list.insert(0, 'Harry')
print(new_list)

new_list.append('Harry')
# remove(value) - Удаление по значению (удаляет первое найденое совпадение)

new_list.remove('Harry')
print(new_list)
new_list.remove('Harry')
print(new_list)
# new_list.remove('Harry')
# print(new_list)
# Если значения которое нужно удалить нет, то будет ошибка

new_list.extend(automation_frontend)
print(new_list)

# pop(index)- Удаление по идексу или последнее из списка

delited_element = new_list.pop() # Без индекса удаляет последнее
print(new_list)
print(delited_element)
# Если значения которое нужно удалить нет, то будет ошибка

first_delited_element = new_list.pop(2)
print(new_list)

# clear() - Очистка списка
# new_list.clear()
print(new_list)

mike_index = new_list.index('Mike')
print(mike_index)

# при обращении вне списка, будет ошибка
# count(value) - сколько раз элемент присутствует в списке
oliver_count = new_list.count('Oliver')
print(oliver_count)

vadim_count = new_list.count('Vadim') # нормально отработает и покажет 0
print(vadim_count)

print(new_list)
# sort() - сортировка списка на месте, т.е. порядок списка изменится
new_list.sort()
print(new_list)

new_list.sort(reverse=True) # сортировка в обратном порядке
print(new_list)

# reverse() - изменение порядка списка (меняет на месте)
new_list.reverse()
print(new_list)

# copy() - копирование списка т.е. создание нового

numbers_list = [1,2,3,4,5,6,7,]
numbers_list_copy = numbers_list
print(numbers_list_copy)
print(numbers_list)
# == проверка равенства значений
print(numbers_list_copy == numbers_list)
print(numbers_list_copy is numbers_list)
# is проверка ссылок(переменные ссылаются на одну и ту же переменную)
numbers_list_copy.append(5)
print(numbers_list_copy)
print(numbers_list)

# список - это ссылочный тип данных
# что бы модефицировть список не изменяя исходное значение нужно создать копию списка
nums_copy = numbers_list.copy()
print(numbers_list == nums_copy)
print(numbers_list is nums_copy)

nums_copy = numbers_list[:]
print(numbers_list == nums_copy)
print(numbers_list is nums_copy)

for nums in numbers_list:
    print(nums)

print(students)
for student in students:
    print(student)

for index, student in enumerate(students):
    print(f'On {index} index is {student} student')