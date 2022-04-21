'''
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''


def summary():
    try:
        with open('file_5.txt', 'w+', encoding='utf-8') as f:
            line = input('Введите цифры через пробел: \n')
            f.writelines(line)
            my_numb = line.split()

        print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Введен некорректный символ')


summary()
