# Создание классов и введение в ООП

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Меня зовут {self.name} и мне {self.age} лет.')

person = Person('Sergo', 31)
person.introduce()

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.pages = year

    def info(self):
        dict_info = {
            'Книга': self.title,
            'Автор': self.author,
            'Год издания': self.pages
        }
        for key, value in dict_info.items():
            print(f'{key}: {value}')


book = Book('Преступление и наказание', 'Ф.Достоевский', 1866)
book.info()

class BankAccount:
    def __init__(self, name:str, balance:float):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Успешное пополнение, ваш баланс {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Не достаточно средств')
        elif amount <= self.balance:
            self.balance -= amount
            print(f'Выдано {amount}, ваш баланс {self.balance}')
        else:
            pass
    def show_balance(self):
        print(f'Ваш баланс {self.balance}')

user1 = BankAccount('Kurolesov Ivan', 0)
user1.show_balance()
user1.deposit(100)
user1.show_balance()
user1.withdraw(1000)
user1.withdraw(99.5)
user1.deposit(100_000)

