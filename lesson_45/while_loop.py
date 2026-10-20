# Знакомство с while

count = 0  # Переменная обявлена до цикла и из за этого она сохраняет свое значение после цикла
while count < 10:  # задаем условие
    print(count) # выполняем сначало действие в цикле потом инкремент
    count += 1  # обязательно инкремент
print(count)



languages = ['Python', 'Ruby', 'Java']

for language in languages:
    print(language)

print('---'*10)

i = 0
while i < len(languages):
    print(languages[i])
    i += 1

# бесконечный цикл автоматически никогда не закончится
# while True:
#     print('Working...')

name = []

while True:
    user_input = input("Введите exit для выхода: ")
    if user_input == "exit":
        break
    name.append(user_input.capitalize())
print(name)

max_value = 10
while max_value > 0:
    print(max_value)
    max_value -= 1