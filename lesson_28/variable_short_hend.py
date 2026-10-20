# Сокращенные операции присваивания
from lesson_5.memory_storage import course

age = 28
age = age + 1
print(age)

# сокращенная форма

# увеличение
year = 2025
year += 1 # year = year + 1
print(year)

# вычитание
balance = 1000
product_prise = 100
balance = balance - product_prise
balance -= product_prise
print(balance)

# ошибка
# x *=1 # NameError: name 'x' is not defined
# print(x)

# увеличение на 25%
course_prise = 40_000
course_prise *= 1.25
print(course_prise)

# деление

amount = 1_000
amount /= 4
print(amount)

total_grade = 70
school_subject = 15
average_grade = total_grade
average_grade /= school_subject
print(average_grade)

# Целочисленное деление
print(88 / 20) # 4.4
print(88 // 20)

summa = 500
summa //= 6
print(summa)

# Остаток от деления %
print(88 % 20) # 4.4
print(88 % 21)

# Возведение в степень **=
initial_capital = 10
initial_capital **= 2
print(initial_capital)

# Работает со строками
full_name = 'Sergei'
full_name += ' Kochkin'
print(full_name)




