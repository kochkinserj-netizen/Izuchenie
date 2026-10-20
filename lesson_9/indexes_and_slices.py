# Работа с индексими и срезами

full_name = 'Sergei Kochkin'
# str - Упорядоченная коллеция символов
# у каждого сивола есть свое место (порядковый номер)

# нумерация начинается всегда с нуля
# индекс - порядковый номер символа
# в жизни отчет с 1, а в разработке с 0

first_letter = full_name[0]
print(first_letter)

second_letter = full_name[1]
print(second_letter)

print(len(full_name))

last_letter = full_name[13] # Не забываем что индексы считаются с 0 т.е. если делать индекс 14 как количество символов то будет ошибка
print(last_letter)

# len(full_name) - 1 вычесление последнего индекса
last_letter = full_name[len(full_name) - 1]
print(last_letter)

#  отсчет с конца начинается с минус 1 [-1]
last_leater = full_name[-1]
print(last_letter)

# второй элемент с конца
print(full_name[-2])

# при обращении к индексу свыше нормы получим IndexError
# print(full_name[100])

print(full_name)

# строка immutable, поэтому будет Error
# full_name[0] = 'v'
# print(full_name)

print(type(full_name[7]))


# срезы - взятие подстроки из исходной строки
# end не входит в выборку
first_name = full_name[0:6]
print(first_name)
last_name = full_name[7:15]
print(last_name)

space_by_index = full_name[6]
print(space_by_index)

space_by_slice = full_name[6:7]
print(space_by_slice)

# можно без энд и старт
first_name = full_name[:6]
print(first_name)
last_name = full_name[6:]
print(last_name)

# если индекс не указывать то будет копия строки
full_name_copy = full_name[:]
print(full_name_copy)

last_5_letter = full_name[-5:]
print(last_5_letter)

last_letter = full_name[-5:-2]
print(last_letter)

# как развернуть строку
reversed_full_name = full_name[::-1]
print(reversed_full_name)

# при работе со срезами при обращению к несуществуещему индексу ошибки не будет
print(full_name[0:100:-1])

# в случае привышения end и start длинны строки срез вернет пустую строку ''
print(full_name[1000:100] == '')

