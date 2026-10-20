# сравнение строк
#  знак равенства читается как "присвоение"
# знак "==" операция сравнения значений
# результатом будет логический тип
'''
role = 'admin'
user_role = input('Введите свою роль: ')
user_role = user_role.strip().lower()
print(user_role)
print(f'Равно ли значение {role} cо значением {user_role} {role == user_role}')
'''
# != - символ не равенства
# результат логический тип

print(23!=15)
print(23!=23)
print('Sergei'!= 'sergei') # Чувствително к регистру
print(len('role') == 0)

print('a'> 'A')
