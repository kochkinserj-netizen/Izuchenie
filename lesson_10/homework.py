# 1 первый и последний символ
variable = 'Sergei Kochkin'
print(variable[0])
print(variable[-1])

# 2 вывести без первого и последнего символа
print(len(variable))
shot_variable = variable
print(shot_variable[1:-1])

# 3  Перевернуть строку
print(variable[::-1])

# 4 Вывести каждый второй символ
print(variable[::2])

# 5 удалить символ по индексу
index = 6
print(variable[:index] + variable[index + 1:]) # добовляем еденицу что бы вывелось

# 6
print(variable[:])

# 7 вернуть предпоследний символ
print(variable[-2])

# 8 удвоить символ
substring = variable[:3]
print(substring*2)
