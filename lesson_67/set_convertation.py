# прелбразование list и tuple на set

users_list = ['Russia','China','Japan','Iran','Korea','Russia','Latvia','China']

# очитска списка от дубликатов
users_set = set(users_list)
print(users_set)

# проверка что список не содержит дубликатов
print(len(users_set)==len(users_list))

'''
Способы конвертации
list <-> tuple
list <-> set
tuple <-> set
'''

# Быстрый поиск
print('Korea' in users_set)
print('Greece' not in users_set)

# set неиндексируемый

# union
a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = a|b
print(c)

# intersection
ab_inter = a&b
print(ab_inter)

# diff -
ab_diff = a-b
print(ab_diff)

# symc dif

ab_symc_diff = a^b
print(ab_symc_diff)
