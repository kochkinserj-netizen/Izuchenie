# Знакомство с циклами

# range(5) = range(0, 5) => 0, 1, 2, 3, 4, 5
for i in range(5):
    print(i)

languages = ['Python', 'Java', 'Ruby', 'PHP', 'Kotlin', 'TypeScript']
for language in languages:
    print(language)

full_name = 'Sergei Kochkin'
for name in full_name:
    print(name)

# цикл while
# нужна переменная для старта отчёта
number = 0
# while хранит условие до кокого значения работает цикл
while number <= 5:
    print(number)
    # внутри while нужно инкраментировать переменную
    number += 1

user_input = int(input('Введите число до которого выполнить цикл: '))

# цикл while
start = 0
while start <= user_input:
    print(start)
    start += 1

# та же реализация с циклом for
for j in range(user_input):
    print(j)

# break - выход из цикла

for k in range(111, 120):
    if k == 115:
        break
    print(k)

# continue - пропуск интерации

for l in range(10):
    if l == 5:
        continue
    print(l)

for i in range(10):
    if i % 2 :
        continue
    print(i)


# вложенные циклы
for i in range(5):
    for j in range(5,10):
        print(i, j)










