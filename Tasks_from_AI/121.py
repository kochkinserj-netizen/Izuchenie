class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Человек: {self.name}, {self.age} лет"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


p = Person("Анна", 25)
print(p)  # Человек: Анна, 25 лет  (вызвался __str__)
print(repr(p))  # Person('Анна', 25)        (вызвался __repr__)