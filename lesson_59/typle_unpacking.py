# Распаковка кортежей

roles = ('admin','manager','director','writer')
print(roles)
admin, manager, director, writer = roles
print(admin)
print(manager)
print(director)
print(writer)

# Количество переменных  при распаковке должно быть равно
# personal, auth_client = roles

admin_role, support_role, *all = roles # оператор в конце
print(admin_role)
print(support_role)
print(all)  # Здесь раворачивание происходит в список

admin, *jops , writer = roles # оператор в середине
print(jops)

*personal, director, writer = roles # оператор в середине
print(personal)

# использование *args


def full_name(name, surname):
    print(f'{name} {surname}')


full_name('Sergei', 'Kochkin')


def get_fio(*args): # аргументы фунции (args) всегда кортеж
    print(args)


get_fio('vadim', 'sergo', 'jon') # аргументы фунции (args) всегда кортеж
