# Обычный
#
# self
#
# объектом
#
# @classmethod
#
# cls
#
# классом
#
# @staticmethod
#
# ничего
#
# независимыми данными

class Car:

    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def info(self):
        print(self.brand)
        print(self.model)

    @classmethod
    def from_string(cls, string):
        brand, model = string.split(',')
        return cls(brand, model)


mashina = Car('Toyota','Camry')
mashina.info()

car = Car.from_string('Toyota,Camry')
car.info()
