# операции над множествами


a = {0, 1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9}

c = {'a', 'b', 'c', 'd', 'e'}
d = {'d', 'e', 'f', 'g', 'h'}

''' методы обновления множеств
- union
- intersection
- difference
- symmetric_differense'''

# Объеденение множеств (union() |)
ab_union = a.union(b)
print(ab_union)

ab_union_v2 = a | b
print(ab_union_v2)

cd_union = c | d
print(cd_union)

# можно сделать union нескольких элементов
abcd_union = a | b | c | d
print(abcd_union)

# Пересечение множеств intersection() или &

ab_intersection = a.intersection(b)
print(ab_intersection)

ab_intersection_v2 = a & b
print(ab_intersection_v2)

# если нет общих значение то будет пустое множество
bc_intersection = b.intersection(c)
print(bc_intersection)

# можно комбинировать методы
abcd_intersection = a & b | c & d
print(abcd_intersection)

# Резность множеств
# Разность создаёт множество элементов, которые есть в первом множестве, но отсутствуют во втором.

ab_difference = a.difference(b)
print(ab_difference)

ba_difference = b.difference(a)
print(ba_difference)

cd_difference = c - d
print(cd_difference)

# Симметричная разность (symmetric_difference()или ^)
# Симметричная разность создаёт множество элементов, которые присутствуют только в одном из множеств, но не в обоих одновременно.
# Создается множество уникальных данных

ab_sym_diff = a.symmetric_difference(b)
print(ab_sym_diff)

cd_sym_diff = c ^ d
print(cd_sym_diff)

#----------------------------------------------------------------------------------------------------------------------
# update () - добавление элементов одного множества в другой
# update () - это union() на месте
a_copy1 = a.copy()
a_copy1.update(b)
print(a_copy1)

# шорт хенд |=
c_copy1 = c.copy()
c_copy1 |= d
print(c_copy1)
print('---'*10)

# intersection_update()
# оставляет в множестве только элементы которые есть в обоих множествах

a_copy2 = a.copy()
a_copy2.intersection_update(b)
print(a_copy2)

# &=
c_copy2 = c.copy()
c_copy2 &= d
print(c_copy2)
print('---'*10)

# difference_update() - разница на месте

a_copy3 = a.copy()
a_copy3.difference_update(b)
print(a_copy3)

# -=
c_copy3 = c.copy()
c_copy3 -= d
print(c_copy3)
print('---'*10)

# symmetric_difference_update() - симетричная разница на месте

a_copy4 = a.copy()
a_copy4.symmetric_difference_update(b)
print(a_copy4)

# ^=
c_copy4 = c.copy()
c_copy4 ^= d
print(c_copy4)
print('---'*10)
