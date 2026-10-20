# Инкапсуляция
# защищаем поля класса от прямого доступа

class Person:
    def __init__(self,name,surname,age):
        # модификаторы доступны : public, protected, private
        # self.attribute - паблик атрибут
        # self.name = name
        # #  protected атрибут (защещенный)
        # self._surname = surname
        # # private атрибут (приват)
        # self.__age = age

        self.__name = name
        self.__surname = surname
        self.__age = age

# getter - получение значения атрибута

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
            return self.__surname

    @property
    def age(self):
        return self.__age

# setter - установка нового значения атрибута

    @name.setter
    def name(self,name):
            self.__name = name

    @surname.setter
    def surname(self,surname):
        self.__surname = surname

    @age.setter
    def age(self,age):
        if age < 0:
            raise ValueError('Age must be >= 0')
        self.__age = age

hl = Person('Harry','Hermione',25)
# print(hl.name)  # К public атрибуту можно обращатся напрямую
# print(hl._surname)  # К protected атрибуту можно обращатся напрямую, но не рекомендованно
# print(hl.__age)  # К private нельзя обратится напрямую

#  Инкапсуляция дает нам полный контроль над логикой работы
#  Мы можем повесить любую логику на getter|setter
print(hl.name)
hl.surname = "George"
print(hl.surname)
