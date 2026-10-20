import csv

# Чтение CSV файла (DictReader)
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# запись в CSV
students = [
    {"name": "Billi", "age": 45, "grade": 5},
    {"name": "Sergont", "age": 70, "grade": 4},
    {"name": "stepan", "age": 18, "grade": 5}
]

with open("report.csv", "a", newline="", encoding="utf-8") as file:
    fieldnames = ["name", "age", "grade"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  #Добовляет заголовки
    writer.writerows(students)