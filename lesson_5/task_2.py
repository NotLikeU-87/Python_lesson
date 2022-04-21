'''
2. Создать текстовый файл (не программно),
сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''
with open('task_2.txt', 'r', encoding='utf-8') as f:
    lines = 0
    letters = 0
    for line in f:
        lines += 1
        letters = len(line.split())
        print(f'Строка: {lines} содержит следующее количество слов: {letters}')
    print(f'Всего строк: {lines}')
