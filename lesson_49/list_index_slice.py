# Доступ к элементам списка по индексам и срезам

users = ['Nick', 'Harry', 'Tommi', 'Bobby', 'Billy']
# Обращение по списку осуществляется variable_name[index]


print(users[0]) # первый элемент

print(users[-1]) # последний элемент

# при обращении по не существующему индексу будет ошибка -> IndexError

# альтернативный способ вызова последнего индекса
print(users[len(users)-1])


# Срезы -> list[start:end:step]
# При взятии
# start - включается , end - не включается/ не входит в срез
print(users)
print(users[2::1]) # со второго идекса до конца

print(users[::2]) # Взятие среза с шагом 2 (По умолчанию шаг 1)
print(users[::-1]) # срез переворачивает список (reverse)
users.reverse() # аналагично [::-1]
print(users)
# Для копирования списка можно использовать срезы или метод copy()
users_copy = users.copy()
print(users_copy)


