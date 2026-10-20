# Вложенные словарь

student = {
    "name": "Sergei",
    "surname":'Kochkin',
    "age":30,
    'is_married':True,
    'partner':{
        'name':'Helga',
        'surname':'Kochkina',
        'age':24
    },
    'address':{
        'country':'Russia',
        'region':'Kirovskaya obl',
        'city':'Kirov',
        'street':'Oktyabrski p-ckt',
        'building':{
            'house': 9,
            'apartment': 7,
        },
    },
    'job': {
        'company':'Big Tech',
        'department':'Big Tech',
        'salary': 1_000_000
    }
}

print(student['name'])
print(student.get('surname'))
print(student.get('car')) # -> None
print(student.get('diposit', 0))

# обращение по ключу -> небезапасно
print(student['address']['city'])
print(student['address']['building']['house']) #-> небезапасный метод

# .get(key,[defoliate_value]) -> безопасно
print(student.get('address', {}).get('building', {}).get('dom', 'No house')) #-> None

# Проверка через in

if 'partner'in student:
    if 'name' in student['partner']:
        print(student['partner']['name'])
else:
    print('no partner')

print(student.get('partner', {}).get('name', '')) # -> тоже в одну строчу

laborer = {}

laborer['name'] = 'John'
laborer.setdefault('surname', 'Simpson')
laborer['job'] = {}

laborer['job']['company'] = 'Big Bank'
laborer['job']['position'] = 'QA'
laborer['job']['salary'] = 500_000
laborer['address']={}
laborer['address']['country'] = 'Russia'
laborer['address']['city'] = 'Kirov'


print(laborer)

for key, value in student.items():
    print(key, value)
