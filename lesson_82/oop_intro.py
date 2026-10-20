# ООП - обьектно ориентированное програмирование
# Классы
student_1 = {
    'id': 1,
    'name': 'Sergo',
    'surname': 'Murata',
}

student_2 = {
    'id': 2,
    'name': 'Martine',
    'surname': 'Coule'
}

student_3 = {
    'id': 3,
    'name': 'Juan',
    'surname': 'Sinck'
}

students = [student_1, student_2, student_3]

# Класс - это станок который выпускает одинаковые детали по шаблону

class Student:
            # у студента три поля : id, name, surname

            # конструктор - функция, которая будет вызыватся при создании нового студента
            def __init__(self, user_id, name, surname):
                self.user_id = user_id
                self.name = name
                self.surname = surname


# обьект - экземпляр класса
wb = Student(5,'Veronica','Korp')
print(wb.user_id)
print(wb.name)
print(wb.surname)


os = Student(15, 'Olga', 'Sidorova')
print(os.user_id)
print(os.name)
print(os.surname)

# Классы ипользуются для создания структур одинакового вида

class Car:
    # brand, model, yaer - атрибуты или поля класса
    def __init__(self,brand,model,year, manufacturer):
                    self.brand = brand
                    self.model = model
                    self.year = year
                    self.manufacturer = manufacturer
    # self - это ссылка на экземпляр класса
    # метод получения данных об авто
    def show_car_info(self):
        return f'Автомобиль марки {self.brand} {self.model} выпущен в {self.year} году'

mercedes = Car('Mercedes','GLE',2020, 'Germany')
print(mercedes.brand)
print(mercedes.model)
print(mercedes.year)
print(mercedes.manufacturer)
print(mercedes.show_car_info())

vaz = Car('АвтоВАЗ', '2107', 1999, 'Russia')
print(vaz.brand)
print(vaz.model)
print(vaz.year)
print(vaz.show_car_info())

print(vaz)

# Прямоугольник Rectangle
# Поля класса : длинна(length), ширина(width)
# методы :
# Получение площади (get_area)
# Периметр (perimeter)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

poll = Rectangle(4,6)
print(poll.area())
print(poll.perimeter())

poll2 = Rectangle(25,25)
print(poll2.area())
print(poll2.perimeter())


# создание банковского счета
# поле депозит - Сумма денег (по умолчанию 0)
# зачесление (сумма пополнения должна быть положительной)
# снятие (нельзя снять с 0 и больше балнса)
# получение баланса

class BankAccount:
    def __init__(self, initial_balance = 0 ):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
          self.balance += amount
        else:
            print('Error, amount cannot be negative')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'ваш баланс {self.balance}')
        else:
            print('Error, amount cannot be more than the balance')

    def get_balance(self):
        return self.balance

print('--------------------------------------')
sber = BankAccount()
print(sber.balance)
sber.deposit(10000)
print(sber.balance)
sber.withdraw(10001)
print('--------------------------------------')
vtb = BankAccount(25_000)
vtb.withdraw(2564)
print(vtb.balance)