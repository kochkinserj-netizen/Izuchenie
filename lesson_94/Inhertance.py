# Наследование

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return 'Voise'

# Наследование - создание одного класса на основе другого
# с возможностью описать в классе родителя методы, которые можно использовать дочерних классах

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return 'Мяу'

class Dog(Animal):
    def __init__(self, name, age, collor):
        super().__init__(name, age)
        self.collor = collor

    #     Полиморфизм - когда один и тот же объект работает в разных классах по разному (переопраделение метода)
    def speak(self):
        return 'гав'


barsik = Cat('barsick', 8 , 'Street cat')
print(barsik.name)

dom = Dog('dominic', 11, 'black')
print(dom.collor)

print(barsik.speak())
print(dom.speak())

