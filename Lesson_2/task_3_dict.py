"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""
season_dict = {1: 'Зима',
               2: 'Зима',
               3: 'Весна',
               4: 'Весна',
               5: 'Весна',
               6: 'Лето',
               7: 'Лето',
               8: 'Лето',
               9: 'Осень',
               10: 'Осень',
               11: 'Осень',
               12: 'Зима'}
month = int(input('Ведите номер месяца: '))
if 1 <= month <= 12:
    print(season_dict.get(month))
else:
    print("такого месяца нет")
