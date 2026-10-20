# name, surname, age, city, is_maried

class Person:
    #  name = 'Sergo' поле класса

    #  Конструктор
    def __init__(self, name, surname, age, city, is_married):
        self.name = name # Атрибут или свойство класса (характеристики)
        self.surname = surname
        self.age = age
        self.city = city
        self.is_married = is_married
        # self - это сыллка на создаваемый обект или экземпляр класса

    #     метод класса (поведение или взаимодействия)
    def get_full_name(self):
        return f'{self.name} {self.surname}'



# экзампляр класса
vz = Person('Sergei', 'Kochkin', 30, 'kirov', True)
print(vz.name)
print(vz.is_married)
vz.age = 31

print(vz.age)
print(vz.get_full_name())

js = Person('John', 'Simpson', 25 , 'NYC', False)
print(js.get_full_name())

# Инкапсуляция - сокрытие атрибутов и взаимодействия с помощью getter|setter
# Наследование - реализация одного класса на оснавании другого
# Полиморфизм - разная реализация одного и того же метода в разных наследниках
# Абстракция - описываем объекты реального мира через свойства и состаяния атрибутов класса