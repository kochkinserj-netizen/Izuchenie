class Person:
    country = 'USA'

    def __init__(self, name: str,surname: str,age:int, city: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
    def get_full_name(self):
        return f'{self.name} {self.surname}'