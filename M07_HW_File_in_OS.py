# Шапка работы
import sys
import os
import time
print ('Created by',sys.version)
print ('Домашнее задание по теме "Файлы в операционной системе"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Примечание в директории должно быть не менее 3-х файлов
# Базовые переменные
filepath = []
files = {}
directory = os.getcwd()
soder = [i for i in os.walk(directory)]
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
file_work = file[2:5]
# Вывод данных
print('Директория для работы:', directory)
print('Файлы для работы', file_work, 'Выбор одного файла:', file[2])
print('Абсолютный путь к выбранному файлу (ver 1):', os.path.abspath(file[2]))
print('Абсолютный путь к выбранному файлу (ver 2):', directory + chr(92) + os.path.join(file[2]))
print('Время создания файла (необработанное, ver 1):', os.path.getmtime(file[2]))
print('Время создания файла (необработанное, ver 2):', time.localtime(os.path.getmtime(file[2])))
print('Время создания файла:', time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(os.path.getmtime(file[2]))))
print('Размер файла:', os.path.getsize(file[2]), 'байт')
print('Относительный путь до файла:', os.path.dirname(file[2]))
print('-'*20)
# Реализация задания объектным методом
    # Класс информации о файле
class file_info():
    def __init__(self,fn):
        self.filepath = os.path.abspath(fn)
        self.filetime = os.path.getmtime(fn)
        self.filesize = os.path.getsize(fn)
        self.parent_dir = os.path.abspath(fn).rstrip(fn)
    # Заполнение словаря объектов: имя файла = создание объекта
for i in file_work:
     files[i] = file_info(i)
    # Вывод информации
for i, j in files.items():
    print(f'Файл: {i}, путь: {j.filepath}')
    print(f'Время создания: {time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(j.filetime))} ({j.filetime})')
    print(f'Размер файла: {j.filesize} байт')
    print(f'Родительская директория: {j.parent_dir}')
    print('-'*20)






