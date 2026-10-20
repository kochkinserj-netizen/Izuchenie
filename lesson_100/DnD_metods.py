# Магические методы
from lesson_100.BankAccount import BankAccount
from lesson_100.Developer import Developer
from lesson_100.Person import Person

# __metod__:__init__,


vz = Person('Sergo',25)

print(vz.name) # vz.__str__()
print(id(vz.age))

print(vz)

print(repr(vz))

sergo = Person('Sergo',30)

print(vz == sergo) #это разные оъбекты

print(id(vz))
print(id(sergo))
print(vz < sergo)
print(vz > sergo)



bac_account = BankAccount(100_000)

jpm_account = BankAccount(150_000)

print(bac_account == jpm_account)

money_amount = bac_account + jpm_account
print(money_amount)


js_dev = Developer(['JS','TS','HTML','CSS','React'])
python_dev = Developer(['Python','Pytest','Playwright'])

print(len(js_dev))
print(len(python_dev))

#__dict__

print(vz.__dict__)
print(len(vz.__dict__))

print(js_dev[5])