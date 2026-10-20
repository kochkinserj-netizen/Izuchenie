# Генерация исключений raise
# Случаии для выброса исключений

# Пользовательский ввод
# user_age = int(input("What is your age?"))

# if user_age < 0:
#     print("Your age isn't a negative number")
#     raise ValueError # Выбрасыват ишибку и останавливает программу
# else:
#     print("Your age is", user_age)
#
# print("Hello World")

# Бизнес логика



def withdraw(balance, amount):
    if amount < 0:
        raise ValueError('нельзя снять отрицательную сумму')
    elif 0 < amount < 100:
        raise ValueError("минимальная сумма снятия 100 рублей")
    elif amount >balance:
        raise ValueError("Недостаточно средств на счете")
    elif amount > 300_000:
        raise ValueError('Максимальная сумма снятия 300_000 рублей')
    else:
        print(f'Снято {amount} рублей')
        print(f'Ваш баланс {balance - amount}')


withdraw(300_000, 300000)