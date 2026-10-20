# Cоздание классов

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'Имя: {self.name}, Возраст: {self.age}')

user1 = Person('Ivan', 33)
user1.show_info()

user2 = Person('Стефания',66)
user2.show_info()

user3 = Person('Halk', 45)
user3.show_info()

class Car:
    def __init__(self, brend, model, year):
        self.brend = brend
        self.model = model
        self.year = year

    def brend(self):
        print(self.brend)

    def model(self):
        print(self.model)

    def year(self):
        print(self.year)

car1 = Car('BMW', 'X5', 2020)
print(car1.brend)
print(car1.model)
print(car1.year)

