"""
6. Реализовать два небольших скрипта:

итератор, генерирующий целые числа,
начиная с указанного;
итератор, повторяющий элементы некоторого списка,
определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл
не должен быть бесконечным.
Предусмотрите условие его завершения.
#### Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие,
при котором повторение элементов списка прекратится.
"""

from itertools import count
from itertools import cycle


def my_count():
    for el in count(3, 2):
        if el > 10:
            break
        else:
            print(el)


my_count()


def my_count_hard(start, stop):
    for el in count(start, 2):
        if el > stop:
            break
        else:
            print(el)


my_count_hard(start=int(input('Введите стартовое число: ')), stop=int(input('Введите конечное число: ')))


def my_cycle(my_list, iteration):
    c = 1
    for el in cycle(my_list):
        print(el)
        c += 1
        if c > iteration:
            break


my_cycle(my_list=input('Введите символы: '), iteration=int(input("Введите количество итераций: ")))
