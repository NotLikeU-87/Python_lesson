'''
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

with open('file_5.txt', 'w+') as f:
    line = input('Введите цифры через пробел: \n')
    f.writelines(line)
    my_numb = line.split()

print(sum(map(int, my_numb)))
