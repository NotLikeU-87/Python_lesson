'''
1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''
with open(r'task_1.txt', 'w', encoding='utf-8') as f:
    while True:
        text = input('Введите данные или оставьте строку пустой: ')
        if not text:
            break
        print(text, file=f)