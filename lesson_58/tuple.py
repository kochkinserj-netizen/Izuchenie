# Что такое tuple -
# Tuple (кортеж) — это упорядоченная коллекция элементов, которая не подлежит изменению.
#
# Главная особенность tuple — его элементы нельзя изменять после создания.
#
# Tuple используется для хранения:
#
# - фиксированных наборов данных
# - координат
# - параметров
# - результатов функций

cities = ('Moscow', 'Kazan', 'Volgograd', 'Krasnodar', 'Ufa', 'Omsk')
print(type(cities))
print(cities)

# К элементам кортежа можно обратится по индексу
print(cities[0])
print(cities[-1])

# Можно взять длинну
print(len(cities))

# Ключевая особенность кортежей в их неизменяемости
# cities[1] = 'New York'
# print(cities)



ids = (35,3543,34,87,442,445,)
diff_values = ('python', 15, True)

roles = ('admin','user', 'support', 'quest')
roles_list = list(roles)
roles_list.append('blocked_user')
roles = tuple(roles_list)
print(roles)

# функция tuple(iterable) - преобразует в кортеж

roles_copy = roles
print(roles_copy)
print(roles)

print(id(roles))
print(id(roles_copy))

print(roles_copy is roles)

roles_copy_list = list(roles_copy)
roles_list.append('student')
roles_list = tuple(roles_list)
print(roles_list)
print(id(roles_list))
