# Значения которые при сравнении возврощают False
# bool(value) -> False


# Полный список falsy values в Python

# False
print(bool(False))

# None
print(bool(None))

# 0, 0.0, 0.j
print(bool(0))
print(bool(0.0))
print(bool(0.j))

# пустая строка
print(bool(''))

# Любой тип данных который пустой словарь,кортеж,список
print(bool([]))
print(bool(()))
print(bool({}))

# set() - пустое множество
print(bool(set()))

# Любое другое значение будет True
print(bool(' '))
print(bool('0'))
print(bool('j'))
print(bool(float('inf')))
print(bool([0]))

# если длинна коллекции ==0, то false value

users = ['Sergo']
if users:
    print('Есть пользователи')
else:
    print('Пользователей нет')

user_name = 'Sergo'
if user_name:
    print(f'Hello {user_name}')
else:
    print('Empty string')


