# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Модули и пакеты"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Подключение функций деления из модулей fake_math и true_math под псевдонимами d_f и d_t
from fake_math import div as d_f
from true_math import div as d_t
# Описание функции передачи и обработки выходных данных
def two_func(dividend,divider):
    print('Функция div из fake_math  - ')
    # Обработка признака нечислового значения для функция div из fake_math
    if d_f(dividend, divider) == None:
        print('Переданы нечисловые значения')
        # Вывод результатов для функция div из fake_math
    else:
        print(d_f(dividend, divider))
    print('Функция div из true_math  - ')
    # Обработка признака нечислового значения для функция div из true_math
    if d_t(dividend, divider) == None:
        print('Переданы нечисловые значения\n')
        # Вывод результатов для функция div из true_math
    else:
        print(d_t(dividend, divider))
# передача различных вариантов данных и вывод результатов
print('Работа функций деления из других модулей при передаче разных данных\n')
frst_par = True
scnd_par = 'XYZ'
print(f'Вариант 1. Оба параметра функций нечисловые, делимое: {frst_par} , делитель: {scnd_par} ')
two_func(frst_par,scnd_par)
frst_par = 10
scnd_par = False
print(f'Вариант 2. Один из параметров функций нечисловой, делимое: {frst_par} , делитель: {scnd_par} ')
two_func(frst_par,scnd_par)
frst_par = 'ABC'
scnd_par = 528
print(f'Вариант 3. Один из параметров функций нечисловой, делимое: {frst_par} , делитель: {scnd_par} ')
two_func(frst_par,scnd_par)
frst_par = 254
scnd_par = 0
print(f'Вариант 4. Делитель ноль, параметры функций, делимое: {frst_par} , делитель: {scnd_par} ')
two_func(frst_par,scnd_par)
frst_par = 6598
scnd_par = 125
print('')
print(f'Вариант 5. Переданы числа, параметры функций, делимое: {frst_par} , делитель: {scnd_par} ')
two_func(frst_par,scnd_par)