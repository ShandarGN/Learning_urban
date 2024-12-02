# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Варианты исходных данных
lst_object_00 = [10, 50.5, '5', 35.1, 'Dragon', [5, 'S']]
lst_object_01 = ('Karamel', 450, 38.78, ('IDDQD', 10, 589.69), 45, {'one' : 999, 'two' : 'BFG'})
lst_object_02 = ['111', '222', '888', '999']
lst_object_03 = []
# Описания спользуемых функий
    # Функция суммирования переданного списка с обработкой ошибок в данных
def personal_sum(lst_obj):
    incorrect_data = 0
    type_incorrect = set()
    sum = 0
    for i in lst_obj:
        try:
            sum = sum + i
        except TypeError:
            incorrect_data = incorrect_data + 1
            type_incorrect.add(type(i))
    if type_incorrect:
        return sum, incorrect_data, type_incorrect
    else:
        return sum, incorrect_data, None
    # Функция нахождения среднего значания на основе переданных данных с дополнительной обработкой ошибки пустых данных
def calculate_average(lst_obj):
    sum = personal_sum(lst_obj)
    try:
        averg = sum[0]/len(lst_obj)
    except ZeroDivisionError:
        return None
    return round(averg, 3), sum[1], sum[2]
    # Функция выполнения работы
def home_work(in_data):
    sum_object = personal_sum(in_data)
    calc_averg = calculate_average(in_data)
    print(f'Сумма: {sum_object[0]}, неверных данных: {sum_object[1]}, типы неверных данных: {sum_object[2]}')
    if calc_averg:
         print(f'Среднее: {calc_averg[0]}')
    else:
        print('Введен пустой список обьектов')
# Выполнение работы с разными наборами данных
print(f'Набор исходных дандых: {lst_object_00}')
home_work(lst_object_00)
print ('-'*20)
print(f'Набор исходных дандых: {lst_object_01}')
home_work(lst_object_01)
print ('-'*20)
print(f'Набор исходных дандых: {lst_object_02}')
home_work(lst_object_02)
print ('-'*20)
print(f'Набор исходных наддых {lst_object_03}')
home_work(lst_object_03)
