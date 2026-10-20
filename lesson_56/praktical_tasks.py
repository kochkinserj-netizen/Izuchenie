#  Практические задачки со списками (list)
# 1
# Добавить число 10 в конец списка.
nums = [1, 2, 3]
nums.append(10)
print(nums)

# 2
# Добавить число 0 в начало списка.
nums = [1, 2, 3]
nums.insert(0,0)
print(nums)

# 3
# Вставить число 99 на позицию 2.
nums = [10, 20, 30, 40]
nums.insert(1,99)
print(nums)

# 4
# Удалить первое значение 5.
nums = [5, 1, 5, 2, 3]
nums.remove(5) # nums.pop(0)
print(nums)

# 5
# Удалить последний элемент списка.
nums = [1, 2, 3, 4]
nums.pop(-1)
print(nums)

# 6
# Удалить элемент с индексом 1.
nums = [10, 20, 30]
nums.pop(1)
print(nums)

# 7
# Посчитать, сколько раз встречается число 2.
nums = [2, 1, 2, 3, 2]
print(nums.count(2))

# 8
# Найти индекс числа 30.
nums = [10, 20, 30, 40]
print(nums.index(30))

# 9
# Проверить, есть ли число 7 в списке.
nums = [1, 2, 3, 4, 5]
print(7 in nums)

# 10
# Очистить список.
nums = [1, 2, 3]
nums.clear()
print(nums)


# 🟡 Средний уровень
# 11
# Отсортировать список по возрастанию.
nums = [5, 2, 9, 1]
nums.sort()
print(nums)

# 12
# Отсортировать список по убыванию.
nums = [5, 2, 9, 1]
nums.sort(reverse=True)
print(nums)

# 13
# Развернуть список.
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)

# 14
# Создать копию списка и добавить в копию число 100.
nums = [1, 2, 3]
nums_copy = nums.copy()
nums_copy.append(100)
print(nums_copy)

# 15
# Объединить два списка в один.
a = [1, 2]
b = [3, 4]
c = a + b
print(c)

# 16
# Добавить элементы списка b в a, не создавая новый список.
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

# 17
# Проверить, есть ли строка "OK" в списке.
statuses = ["FAIL", "OK", "ERROR"]
print('OK' in statuses)

# 18
# Удалить из списка первое вхождение строки "ERROR".
statuses = ["OK", "ERROR", "FAIL", "ERROR"]
statuses.remove('ERROR')
print(statuses)

# 19
# Найти, сколько раз встречается "PASS".
results = ["PASS", "FAIL", "PASS", "PASS"]
print(results.count('PASS'))

# 20
# Добавить элемент "DONE" в конец списка, если его там нет.
statuses = ["NEW", "IN_PROGRESS"]
if 'DONE' not in statuses:
    statuses.append("DONE")
    print(statuses)
else:
    print("DONE есть в списке")

# 🔴 Продвинутый уровень
# 21
# Удалить все значения 0 из списка.
nums = [0, 1, 0, 2, 3, 0, 4]
for num in nums:
    if num == 0:
        nums.remove(0)
print(nums)


# 22
# Создать новый список, содержащий только чётные числа.
nums = [1, 2, 3, 4, 5, 6]
even = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
print(even)

# 23
# Заменить все значения 1 на 100.
nums = [1, 2, 1, 3, 1]
nums1 =[]
for n in nums:
    if n == 1:
       nums1.append(100)
    else:
       nums1.append(n)
print(nums1)

# 24
# Найти максимальное значение списка.
nums = [5, 9, 2, 11, 3]
print(max(nums))

# 25
# Найти минимальное значение списка.
nums = [5, 9, 2, 11, 3]
print(min(nums))

# 26
# Проверить, отсортирован ли список по возрастанию.
nums = [1, 2, 3, 4]
print(nums == sorted(nums))

# 27
# Создать список квадратов чисел.
nums = [1, 2, 3, 4]
sqares = []
for num in nums:
    sqares.append(num ** 2)
print(sqares)

# 28
# Удалить дубликаты из списка.
nums = [1, 2, 2, 3, 1, 4]
nums = list(set(nums))
print(nums)

# 29
# Разделить список на два: чётные и нечётные.
nums = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)

# 30
# Найти второй по величине элемент.
nums = [5, 1, 9, 3, 7]
print(sorted(nums)[-2])