class Person:
    # name, surname, age, city
    #  get_fio
    def __init__(self,name, surname, age, city):  # конструктор
        # self - это ссылка на объект
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

    def get_full_name(self):
        return f'{self.name} {self.surname}'

vz = Person('Ivan','Kurolesov', 29,'Kirov')
print(vz.name)
print(vz.surname)
print(vz.age)

wb = Person('Wade', 'Barker', 28, 'Moscow')
print(wb.get_full_name())

pp = Person('Peter', 'Parker', 25, 'NYC')


jon = 'jon'
print(jon)