# шапка задания
import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Функции в Python.Функция с параметром"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*16)
# блок определений
    # задание функции формирования и заполнения матрицы.
def get_matrix(n=3, m=3, value='NA'):
        # входные аргументы - число строк (по умолчанию 3) и столбцов (по умолчанию 3), значание для заполнения (по умолчанию NA)
    matrix = [] # пустая итоговая матрица
    column_m = [] # строка матрицы
    for i in range(m): # заполнение строки значениями
        column_m.append(value)
    for j in range(n): # заполнение матрицы строками
        matrix.append(column_m)
    return matrix # выходные данные - итоговая матрица
# блок ввода исходных данных
print ('Внимание, при вводе числа больше 9 для заполнения будет использоваться значение 9')
print ('При вводе числа меньше единицы в число строк или столбцов, программа вернет пустую матрицу')
    # ввод числа строк, число больше 9 будет считаться 9
n = int(input('Введите число строк: '))
if n >= 10:
    n = 9
    # ввод числа столцов, число больше 9 будет считаться 9
m = int(input('Введите число столцов: '))
if m >= 10:
    m = 9
    # ввод содержимого матрицы, для заполнения будет использовано не более 3-х символов
value = str(input('Введите содержимое матрицы, для заполнения будет использовано не более 3-х символов: ')[:3])
# блок вывода задания, выполнения и вывода итогов
    # проверка введенных значений числа строк и столбцов матрицы
if n > 0 and m > 0: 
    # вывод задания на заполенние
    print(f'Итоговая матрица строк - {n}, столбцов - {m}, заполненная значенями - {value}')
    # генерация и заполнение матрицы
    matrix01 = get_matrix(n, m, value)
    # вывод матрицы в виде таблицы
    for i in range(n):
        print(matrix01[i])
else:
    # создание пустой матрицы для выводы при нулевом значении одного из параметров матрицы
    matrix_null = []
    print ('Один из параметров матрицы равен нулю, вывод пустой матрицы -',matrix_null)
