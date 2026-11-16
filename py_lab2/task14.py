b_year = int(input('Введите год рождения: '))
b_month = int(input('Введите месяц рождения: '))
b_day = int(input('Введите день рождения: '))

c_year = int(input('Введите текущий год: '))
c_month = int(input('Введите текущий месяц: '))
c_day = int(input('Введите текущий день: '))

age = c_year - b_year

if (c_month < b_month) or (c_month == b_month and c_day < b_day):
    age -= 1

print(f"Возраст человека (полных лет): {age}")
