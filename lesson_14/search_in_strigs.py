# поиск в строках

full_name = 'Sergei Kochkin'

#  count() — сколько раз подстрока встречается в строке
count_leter_e = full_name.count('e')
print(count_leter_e)
count_leter_s = full_name.count('s')
print(count_leter_s) # Регистр имеет значение

count_leter_s_2 = full_name.lower().count('s') # переводим все в нижний регистр а потом ищем. все работает
print(count_leter_s_2)

count_leter_s_3 = full_name.upper().count('S')
print(count_leter_s_3)

count_letter_in = full_name.count('in')
print(count_letter_in)

count_e_by_index = full_name.count('e',2) # Начинается отчет от указаного символа
print(count_e_by_index)

no_match = full_name.count('no') # при отсутствии совподений будет 0
print(no_match)

text = 'aaa'
count_a = text.count('aa') # При пересечении он находит один раз
print(count_a)

# index() — ищет подстроку и возвращает её позицию (индекс)

full_name = 'Sergei Kochkin'
first_index = full_name.index('e')
print(first_index)

index_by_in = full_name.index('in')
print(index_by_in)
index_by_start = full_name.index('e',2) # Возвращает индекс полной строки
print(index_by_start)

# при поиске по отсутсвуещей подстроке будет ошибка  ValueError
'''
index_by_z = full_name.index('z')
print(index_by_z)
'''
# find() — ищет подстроку, но безопасно работает точно так же как и .index только если нет подстроки возврощает -1

index_by_z = full_name.find('z')
print(index_by_z)

index_by_in = full_name.find('in')
print(index_by_in)

# rfind() — поиск справа (индекс последнего вхождения)

index_by_last_i = full_name.rfind('i')
print(index_by_last_i)
index_by_i = full_name.find('i')
print(index_by_i)

"""
"mississippi".count("ss") → 2
"abracadabra".index("bra") → 1
"hello".find("x") → -1
"banana".rfind("na") → 5
"aaaa".count("aa") → 2
"python".index("t") → 2
"""
print("mississippi".count("ss"))
print("abracadabra".index("bra"))
print("hello".find("x"))
print("banana".rfind("na"))
print("aaaa".count("aa"))
print("python".index("t"))
