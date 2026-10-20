
child = {1,3,7}
not_child = {5,9,-3,0}
parent = {0,1,2,3,4,5,6,7,8,9}

# является ли одно множество подмножеством другого
# Метод issubset()
# Метод проверяет, все ли элементы одного множества находятся в другом.

print(child.issubset(parent))
print(not_child.issubset(parent))

# Метод issuperset()
# Проверяет, является ли множество надмножеством другого.

print(parent.issuperset(child))
print(parent.issuperset(not_child))

# Метод isdisjoint()
# Проверяет, не имеют ли два множества общих элементов.
# Он возвращает True, если множества не пересекаются (их пересечение пустое), и False в противном случае.

a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = {0,9}

ab_inter = a&b
print(ab_inter)
print(a.isdisjoint(b))

ac_inter = a&c
print(ac_inter)
print(a.isdisjoint(c))