class Person:

    def __init__(self, name, age): # __init__ Один из самых частых методов
        self.name = name
        self.age = age

    # def __str__(self)-> str:   # добавление строкового представления магическим методом предопределило информацию,подходит для пользователя
    #     return self.name
    #
    def __repr__(self)-> str: # представление обекта для разработчика
        # обект какого класса был создан и с какими полями
        return f'Person(name={self.name}, age={self.age})'


    def __eq__(self, other):  # сравнение объектов (vz == sergo)
        return self.name == other.name and self.age == other.age


    def __lt__(self, other)-> bool:  # метод сравнение
        return self.age < other.age

