# Встроенные функции для работы с числами

# abs() - модуль числа
num = 5
num1 = -6
num2 = -5.545
print(abs(num))
print(abs(num1))
print(abs(num2))

# max() - min() - минимальное и максимальное значение

print(max(1,2,3,4,5,6,7,8,9,10))
print(min(1,2,3,4,5,6,7,8,9,10))

list = [0.54,45,-65,5,-45,1554.545,0.66565656,-1450]
print(max(list))
print(min(list))

# sum() - сумма в списке
print(sum(list))
print(sum(list,100))

# divmod() - деление и остаток

print(divmod(17, 3))
