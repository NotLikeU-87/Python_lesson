"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(x, y, z):
    arg = [x, y, z]
    sum_max = []
    max_1 = max(arg)
    sum_max.append(max_1)
    arg.remove(max_1)
    max_2 = max(arg)
    sum_max.append(max_2)
    return sum(sum_max)


print('Cумма наибольших двух аргументов:', my_func(int(input('ВВедите первое число: ')), int(input('ВВедите второе число: ')),
        int(input('ВВедите третье число: '))))
