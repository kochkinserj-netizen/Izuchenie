import math
# Полезные методы работы с числами

num1 = 5.0
num2 = 5
num3 = 5.12

print(num1 == num2)

# .is_integer() - применяется к float -> True/False

print(num1.is_integer())
print(num2.is_integer())
print(num3.is_integer())

print(math.floor(num1) == num1)
print(math.floor(num2) == num2)
print(math.floor(num3) == num3)

# Форматирование чисел в f-строках
# :_ разделитель тысяч
mln = 1_000_000
formated_mln = f'{mln:_}'
print(formated_mln)

# :.2f количество чисел после запятой
PI = math.pi
print(PI)
print(round(PI, 2))
print(f'{PI:.2f}')
