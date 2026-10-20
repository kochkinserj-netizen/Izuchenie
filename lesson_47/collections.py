# Знакомство с коллекциями

# В Python есть 4 базовых типа коллекций:
# list - список
# tuple - кортеж
# set - множество
# dict - словарь


# 1. list (список) - упорядоченная изменяемая коллекция.

technologies = ['Python', 'Pytest', 'Playwrigh', 'Github', 'FastAPI']
print(technologies)
print(type(technologies))
print(technologies[0]) # Каждый элемент списка имеет свой индекс по которому можно вызвать его

# Списки изменяемы т.е. можем  добовлять, изменять, заменять
technologies.append('SQLAlchemy')
print(technologies)

technologies.insert(1, 'Pydantic')
print(technologies)

# Списки могут хранить разные типы данных
dif_types_list = [1, 'sds', True]

# 2. tuple (кортеж) - упорядоченная неизменяемая коллекция
roles = ('admin', 'manager', 'user', 'quest')
print(roles)
print(type(roles))
print(roles[-1])

# кортеж неизменяем
# roles[0] = 'blocked_user'

# преобразование в list и обратно в tuple для измениния содержимого
roles_list = list(roles)
print(type(roles_list))
roles_list.append('blocked_user')
roles = tuple(roles_list)
print(roles)
print(type(roles))

# 3. set (множество) - Неупорядоченная колекция уникальных элементов

cities = {'Moscow', 'Kazan', 'Vladivostok', 'Moscow', 'Krasnodar'}
print(cities)

cities.add('Kirov')
print(cities)

products = ['хлеб', "масло", "хлеб", "чай"]
products_set = set(products)
print(products_set)
products = list(products)
print(products)

# 4. dict(словарь) - Коллекция пар ключ-значения.

user = {
    'id': 1,
    'name': 'Sergei',
    'surname': 'Kochkin',
    'is_married': True,
    'friends': ['Alex', 'Artem']
}
print(user)

# В словаре доступ осуществляется через ключи

print(user['name'])
print(user.get('name'))
# При обращенни к несуществующему ключю будет error

user['id'] += 1
print(user)

empty_set = set()
empty_dict = {}
print(type(empty_set))
print(type(empty_dict))

