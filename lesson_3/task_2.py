"""
2. Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def my_func(name, surname, year, town, email, tel):
    return '  '.join([name, surname, year, town, email, tel])


print(my_func('Leo', 'Gol', '1980', 'London', 'email@email.com', '+79452344565'))
print(my_func(surname='Gol', name='Leo', year='1980', town='London', tel='+79452344565', email='email@email.com'))
