# Импорт необходимых библиотек
from multiprocessing import Pool
import time
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Многопроцессное программирование"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
file_name = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
# Описание функции read_info (входные данные - имена файлов)
def read_info(name):
    all_data = []
    with open(name, 'r') as file_in:
        while True:
            line = file_in.readline()
            if not line:
                break
            all_data.append(line)
    print(f'Закончена обработка файла {name}')
# Линейный вызов функции read_info, с замером и выводом времени
start = time.time()
for i in file_name:
    read_info(i)
end = time.time()
print(f'{round(end - start, 3)} секунд')
# Мультипроцессорная часть
if __name__ == '__main__':
    # Мультипроцессорный вызов функции read_info, с замером и выводом времени
    start = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, file_name)
    end = time.time()
    print(f'{round(end - start, 3)} секунд')


