# Работа с файлами

# with - контекстный менеджер

'''
Работа с файлами
open(file_path, mode) - функция которая читает файлы
Режимы (mode):
'r'     read        Чтение (режим по умолчанию)                                 FileNotFoundError
'w'     write       Перезапись (полностью стирает содержимое и добавляет новое) Создание нового файла
'a'     append      Добавление в конец файла                                    Создание нового файла
'x'     exclusive   Создаение нового файла                                      Ошибка если уже файл есть
'b'     binary      Для работы с картинками,видео,аудио
'+'     'r+'        Для чтения и записи одновремено
'''

# старый подход

f = open('resume.txt', 'r')
text = f.read()
print(text)
f.close()

# Новый подход
with open('resume.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

# Файл дерикторией выше
with open('../file.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

# Файл в другом пакете
with open('../lesson_94/file_with_lesson_95.txt', 'r', encoding='utf-8') as file:
    file_text = file.read()
    print(file_text)


# Чтение файлов

# read() - прочитать все содержимое файла в одну строчку
with open('resume.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

# readline() - прочитать одну сторочку с переходом на слудущую
with open('resume.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    print(text)

# readlines() - прочитать все строчки с сохранением в список
with open('resume.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)
    print(text)

# Как работать с большими данными (Большие файлы следует читать через цикл for)
with open('resume.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
