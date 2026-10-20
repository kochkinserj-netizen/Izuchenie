from datetime import datetime, date, time , timedelta


# Что такое datetime
# datetime — стандартный модуль Python для работы:
#
# с датами;
# со временем;
# с датой + временем;
# с разницей между датами;
# с часовыми поясами;
# с преобразованием дат в строки и обратно.


t = date.today()
print(t)

print(t.day)
print(t.month)
print(t.year)
print(t.weekday()) # день недели с пн - 0
print(t.isoweekday()) # день недели с пн - 1

# isocalendar год, день недели,неделя
print(t.isocalendar())
birthday = date(1926, 11 , 29)
print(birthday)


# time
t1 = time(13,12,55)
print(t1)

# datetime

now = datetime.now()
print(type(now))
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.day)
print(now.month)
print(now.year)
print(now.weekday())
print(now.isoweekday())
print(now.isoformat())

# Сравнение дат

print(birthday < t)

# timedelta

tomorrow = date.today() - timedelta(days=1)
print(tomorrow)


print(t - birthday )

diff = t - birthday
print(diff)


# strftime() - фгорматировани даты


print(t.strftime("%d.%m.%Y"))

# strptime - Преобразование строки в дату
date_string = "20.08.2026"
print(type(t))
print(type(date_string))

str_to_time = datetime.strptime(date_string, "%d.%m.%Y")
print(str_to_time)



















