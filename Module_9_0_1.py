# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашнее задание по теме "Введение в функциональное программирование"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
a = [25, 56.8, 986, 519.8, '5', True, 'abc']
func_bullin = [min, max, len, sorted]
# Определение функции высшего порядка
def apply_all_func(int_list, *functions):
    err_nom = []
    valid_lst = []
    result = {}
    # Печать исходных данных
    print('Исходные функции: ')
    print([i.__name__ for i in functions])
    # Проверка типа элементов переданного списка и формирование списка валидных элементов
    for i in int_list:
        if type(i) not in [int, float]:
            err_nom.append(int_list.index(i))
        else:
            valid_lst.append(i)
    # Первый вариант обработки списка
    print('Вариант отмены расчета при наличии нечисловых элементов в списке:')
    if err_nom:
        print(f'В списке: {int_list}')
        print(f'Есть нечисловые элементы, их номера: {err_nom}\n')
    else:
        for i in functions:
            result[i.__name__] = i(int_list)
    # Второй вариант обработки списка
    print('Вариант расчета на основании списка с удаленными нечисловыми элементами:')
    print(f'Исходный список: {int_list}')
    print(f'Список для расчета: {valid_lst}')
    if valid_lst:
         for i in functions:
             result[i.__name__] = i(valid_lst)
    return result
# Вывод итогов
print('Передача перечня функций')
print(f'{apply_all_func(a, min, max, len, sorted)}\n')
print('Передача списка функций')
print(apply_all_func(a,  *func_bullin))
