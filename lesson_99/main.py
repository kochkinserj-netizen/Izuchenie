from lesson_99.Person import Person

ik = Person('Ivan','Kurolesov', 33, 'Los Angeles') # вызывается Person().__init__def .....
print(ik.name)
print(ik.age)

sk = Person('Sky','Knopin', 33, 'Kirov')

print(sk.name)
print(sk.country)

print(sk.get_full_name())
print(ik.get_full_name())
