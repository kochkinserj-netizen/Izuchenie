import json
student = {
    "name": "Anna",
    "age": 20,
    "grade": 5
}

#  json.dumps() Преобразование словаря в JSON - сериализация

json_data = json.dumps(student, ensure_ascii=False)
print(json_data)  # '{"name": "Anna", "age": 20, "grade": 5}'
print(type(json_data))


teacher = {
    'name': 'Вадим',
    'surname': 'Звягинцев'
}

json_data = json.dumps(teacher, ensure_ascii=False)
print(json_data)
print(type(json_data))



#  json.loads() Парсинг JSON

json_data = '{"name": "Anna", "age": 20, "grade": 5}'

student = json.loads(json_data)

print(student)
print(student["name"])

# Чтение файла JSON через load

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    print(student["name"])

# чтение через dump

loosers = [
    {
        "name": "Harry",
        "age": 24,
        "grade": 2
    },
    {
        "name": "Billy",
        "age": 25,
        "grade": 3
    }
]
with open("bad_students.json", "a", encoding="utf-8") as file:
    json.dump(
        loosers,
        file,
        ensure_ascii=False,
        indent=4
    )