# Знакомство с операторами прерывания и пропуска цикл

# break
print('before loop')

for i in range(25,35):
    if i == 30:
        break
    print(i)

print('after loop')

languages = ['Python', 'Java', 'TypeScript','Ruby']
java_index = None

for leng in languages:
    if leng.lower() == ('typescript'):
        java_index = languages.index(leng)
        break
    print(leng)

print(f'java_index is {java_index}')

# continue

for i in range(10):
    if i == 2:
        continue
    print(i)


balances = [100, 0, -250, 75, 300, -400]

positiv_balances = 0

for i in range(len(balances)):
    if balances[i] <= 0:
        continue
    positiv_balances += balances[i]

print(positiv_balances)



while True:
    user_input = int(input('Введите положительное число: '))
    if user_input <= 0:
        break
    print(f'Все ок, ты ввел: {user_input}')
if user_input < 0:
    print(f'Упс, ты ввел {user_input}, это отрицательное число')
else:
    print('Ого ты проверил ZERO!')

