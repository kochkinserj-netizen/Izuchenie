# повторение удаления (обрезки символов)

'''Удалить пробелы, табы и переносы строки:

"   Hello \n world \t "'''

text = "Hello \n world \t "
print(text.strip())

'''
Задача 2
Из строки

"...ERROR..."
получить

"ERROR"
'''

message = '......ERROR......'
print(message.strip('.'))

'''
Из строки

"#######login####"
убрать # только справа
'''

string = "#######login####"
print(string.rstrip('#'))

'''
Задача 4
Привести email к нормальному виду:

"   VADIM_zviagintsev@MAIL.rU\n"
Ожидаемый результат:

vadim_zviagintsev@mail.ru
'''
email = "   VADIM_zviagintsev@MAIL.rU\n"
print(email.lower().strip())

'''
Задача 5
Убрать только точки в конце строки:

"version 1.2.3...."
'''

text = "version 1.2.3...."
print(text.strip('.'))


