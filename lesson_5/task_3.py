'''
3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''
with open('task_3.txt', 'r', encoding='utf-8') as f:
    names = []
    all_salary: int = 0
    employs = 0
    for line in f:
        employs += 1
        name, salary = (i for i in line.split())
        if float(salary) < 20000:
            names.append(name)
        all_salary += float(salary)
    all_salary /= employs
print(f'Сотрудники получаюшие менее 20 тысяч: {[*names]}')
print(f'Cредний доход сотрудников:  {all_salary}')
