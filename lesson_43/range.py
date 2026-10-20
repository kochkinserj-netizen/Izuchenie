# Знакомства с range
# range() - Функция последовательности чисел

print(type(range(101)))

# Генерация чисел от старта до указаного значения, при том указанное значение не входит
for i in range(10):
    print(i)

# range(start, stop, step)
# stop - не включается в последовательность

for i in range(0, 5, 1):
    print(i)

for i in range(0, 10, 2):
    print(i)

# step - если мы указываем шаг , то необходимо указывать все значения range
for i in range(0, 10, 2):
    print(i)

# если мы идем по убыванию то ставим в step "-" и обязательно stop < start, иначе ничего не заработает
for i in range(10, 0, -1):
    print(i)

# из range можно сделать list()
print(list(range(10)))

countries = ['russia', 'india', 'china', 'japan', 'canada']
for country in countries:
    print(country.capitalize())

print(len(countries))

# range(len(countries)) -> range(6)
for i in range(len(countries)):
    print(i)
    print(countries[i])


# Практика из урока

for j in range(10):
    print(j)

for j in range(5,16):
    print(j)

for j in range(0,21,2):
    print(j)

for j in range(10,0,-1):
    print(j)