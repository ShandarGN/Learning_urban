# Импорт необходимых библиотек
import sys
    # Установка библитеки numpy
import numpy as np
    # Установка библиотеки pillow (PIL)
from PIL import Image
from PIL import ImageFilter
    # Установка библиотеки pandas
import pandas as pd
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Обзор сторонних библиотек Python"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Блок работы с библиотекой numpy
print('Некоторые возможности библиотеки numpy')
    # Исходные данные
array_1 = np.array([5, 2, 6, 9])
array_2 = np.array([[8, 3, 1, 7], [8, 4, 2, 2], [5, 9, 2, 3]])
lst_arr = [array_1, array_2]
    # Функция arr_oper принимает массив и код операции (oper)
        # Коды операций:
            # 1 - возвращает минимальное и максимально значение массива arr
            # 2 - позиции минимального и максимально значения в массиве arr
            # 3 - возвращает транспонированный массив arr1
            # 4 - возвращает сумму массива arr
            # 5 - возвращает размерность массива arr
            # 6 - возвращает число строк и столбцов массива arr
            # 7 - прибавляет к массиву arr число num
            # 8 - умножает массив arr на число num
def arr_oper(arr, oper, num = None):
    if oper == 1:
        return f'Максимальное {arr.max()} и минимальное значение {arr.min()}'
    elif oper == 2:
        return f'Позиция максимального элемента {arr.argmax()} и минимального {arr.argmin()}'
    elif oper == 3:
        return f'Транспонированный массив \n {arr.T}'
    elif oper == 4:
        return f'Сумма массива {arr.sum()}'
    elif oper == 5:
        return f'Размерность массива {arr.ndim}'
    elif oper == 6:
        return f'Размер массива {arr.shape} строк и столбцов'
    elif oper == 7 and type(num) in [float, int]:
        return f'Сложение массива с числом {num} \n {arr + num}'
    elif oper == 8 and type(num) in [float, int]:
        return f'Умножение массива на число {num} \n {arr * num}'
    # Обработка исходных данных
for j in lst_arr:
    print(f'Исходный массив \n{j}')
    for i in range(1, 9):
        print('     *',arr_oper(j, i, 8))
    print('-' * 20)
# Блок работы с библиотекой pillow (PIL)
print('Некоторые возможности библиотеки pillow (PIL), см. результаты')
    # Картинки для работы - fox.jpg и bear.jpg
lst_name = ['fox.jpg', 'bear.jpg']
dict_img = {}
    # Создание словаря открытых файлов
for i in lst_name:
    var_name = i[0: i.find('.')] + '_img'
    dict_img[var_name] = Image.open(i)
    # Демонстрация методов и сохранение результатов
for i, j in dict_img.items():
        # Поворот на 180 градусов
    oper = j.rotate(180)
    oper.save(f'r_{i}.jpg')
        # Фильтр размытие
    oper = j.filter(ImageFilter.BLUR)
    oper.save(f'fb_{i}.jpg')
        # Сохранение в другом формате
    oper.save(f'spng_{i}.png', 'png')
        # Преобразование в черно-белый рисунок
    oper = j.convert('L')
    oper.save(f'bw_{i}.jpg')
        # Изменение размера
    oper = oper.resize((300, 300))
    oper.save(f'rsz_{i}.jpg')
print ('-'*20)
# Блок работы с библиотекой pandas
print('Некоторые возможности библиотеки pandas')
    # Исходные данные
dict_data = {'Garry' : 125.51, 'Den' : 55.77, 'Max' : 213.54, 'Jon' : 98.04, 'Alice' : 51.03, 'Ravena' : 71.07}
    # Создание серии из списка и словаря
series_int = pd.Series([4, 3, 20, 2, 19, 14, 18, 14, 9, 4, 20, 3, 1, 20, 2])
series_float = pd.Series(dict_data)
    # Вывод созданных объектов
print(f'Серия series_int\n{series_int}')
print(f'Серия series_float (из словаря)\n{series_int}')
    # Операции с сериями
        # Отбор и арифметические операции
print(f'Серия series_int - отбор больше 10\n{series_int[series_int > 10]}')
print(f'Серия series_float (деление и округление)\n{round(series_float / 12, 2)}')
print(f'Уникальные данные(1): {series_int.unique()}')
print(f'Уникальные данные с их количеством(2):\n {series_int.value_counts()}')
    # Операции с dataframe
        # Импорт из внешнего файла и установка индексного поля
pln_df = pd.read_csv('planets.csv', sep = ',')
pln_df.set_index('id', inplace=True)
        # Вывод длины и типов данных фрейма
print(pln_df, '\nДлина:', len(pln_df))
print(pln_df.dtypes)
        # Вывод первых и последних значаний фрейма (по умолчанию 5)
print(pln_df.head())
print(pln_df.tail())
        # Вывод простых статистических данных фрейма - количество, минимальное и максимальное и так далее
print(pln_df.describe())
        # Создание и вывод серии на основе фрейма
ser_pln_name = pd.Series(pln_df['Satellites'].tolist())
print(ser_pln_name)
        # Вывод фрейма отсортированного по полю Satellites
print(pln_df.sort_values('Satellites', ascending=False).head(len(pln_df)))
        # Вывод строки заголовка фрейма
print(pln_df.columns.tolist())
        # Вывод вариантов отбора данных
print(pln_df[pln_df['Satellites'].isin(range(5, 10))])
print(pln_df[pln_df['Satellites'] > 20])
        # Вывод группировки по полю Satellites
print(pln_df.groupby('Satellites').count())
        # Создание и вывод сводной таблицы на оснофе фрейма
tmp_pln_df = pln_df.copy()
tmp_pln_df.sort_values('id', inplace=True)
tmp_pln_df = tmp_pln_df[tmp_pln_df.Satellites > 10]
tmp_pln_df = tmp_pln_df[tmp_pln_df.Diameter > 12756.3]
print(tmp_pln_df)