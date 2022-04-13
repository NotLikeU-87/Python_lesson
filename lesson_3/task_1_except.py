# except
def my_div_2(x, y):
    try:
        return int(x) / int(y)
    except ZeroDivisionError:
        print('на ноль делить нельзя')
    except ValueError:
        print('Введите целые числа')


print(my_div_2(input('Введите первое число: '), input('Введите второе число: ')))
