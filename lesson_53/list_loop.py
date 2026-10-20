# Списки в циклах и функциях

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for n in numbers:
    sum += n

print(sum)

negative_nums = []
random_nums = [-3,0,45,12,5,-45,-7]
for n in random_nums:
    if n < 0:
        negative_nums.append(n)

print(negative_nums)

# Работа в циклах со вложенными списками

points = [[1, 2], [3, 4], [5, 6]]

for n in points:
    print(n)
# [1, 2]
# [3, 4]
# [5, 6]

for x, y in points:
    print(f'x={x}, y={y}')
# Здесь происходит распаковка
# x=1, y=2
# x=3, y=4
# x=5, y=6


# enumerate(list)- Функция позволяющая обращатся к индексам и значениям списка
colors = ['red', 'green', 'blue']

for index, value in enumerate(colors):
    print(f'index={index}, color={value}')

# Передача списка в функцию

for n in numbers:
    print(n)


def show_numbers(lst):
    for num in lst:
        print(num)


show_numbers(numbers)


def calculate_sum(*args):
    print(args)
    print(type(args))
    summa = 0
    for n in args:
        summa += n
    print(summa)
calculate_sum(1,2,3,4,5)