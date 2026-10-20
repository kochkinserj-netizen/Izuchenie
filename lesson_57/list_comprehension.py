# list comprehension

numbers = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)

square_numbers = [n ** 2 for n in numbers]
print(square_numbers)


even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)

# list comprehension
even_nums = [n for n in numbers if n % 2 == 0]

# Синтаксис:
#
# even_nums = [         n           for n           in numbers          if n % 2 == 0]
# new_list = [          выражение   for элемент     in старый_список    if условие]
# выражение — значение, которое попадёт в новый список
# for элемент in старый_список — перебор элементов
# if условие — необязательная фильтрация


# Пример

nums = [1,2,3,4,5]

doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)

doubled_nums = [n*2 for n in nums ]
print(doubled_nums)

# list comprehension часто ипользуется во время фильтрации списков

nums = [0,1,3,0,0,1,0,48,0,14,0]
none_zero = [n for n in nums if n != 0]
print(none_zero)

# list comprehension всегда создает новый список
numbers_list = [1,0,25,45,20,0,46,0,-4,-15,0,45]
print(numbers_list)
numbers_list = [n for n in numbers_list if n != 0]
print(numbers_list)

words = ['hi', 'hello', 'Python', 'ai']
long_words = [n for n in words if len(n) > 5]
print(long_words)