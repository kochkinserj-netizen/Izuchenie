# ООП — объектно-ориентированное программирование
# Класс — это шаблон, по которому создаются объекты.

# класс - станок
# объект - деталь

# class
class Person:
    # атрибут класса - хронит состояние класса
    name = 'Ivan'
    age = 28

# Метод — это функция, которая принадлежит объекту или классу.
    def work(self):
        print('Иди работать')

    def eat(self):
        print('Пошел есть')

    def take_reast(self):
        print('Время на отдых')



# object

vz = Person() # экземпляр класса
print(vz.name) # можно обращатся к атрибутам
vz.city = 'Sochi' # можно задавать атрибуты/значение
print(vz.city)

wb = Person()
print(wb.age)
wb.name = ''
print(wb.name) # можно заменить значение

pp = Person()
print(pp.name)
print(pp.age)

