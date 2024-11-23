# импорт необходимых библиотек
import sys
from pprint import pprint
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Позиционирование в файле"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
name00 = 'simple.txt'
strings_in = ['Первая строка_0','Вторая строка_00','Третья строка_000','Четвертая строка_0000']
print('Исходные данные:')
pprint(name00)
pprint(strings_in)
print ('-'*20)
# Описание функции custom_write (запись в файл, принимает имя файла и список записываемых строк)
def custom_write(file_name, strings):
    pos = {}
    # Проверка открытия file_name
    try:
        file = open(file_name, 'a')
    except:
        # Проверка неудачна
        return print(f'Файл {name00} нельзя открыть')
    else:
        # Проверка успешна
        for i in range(0, len(strings)):
            # Словарь pos, ключ номер строки и номер курсора в файле, значение - записанная строка
            pos[(i, file.tell())] = strings[i]
            file.write(strings[i])
            file.write('\n')
        file.close()
        return pprint(pos)
# Применения функции custom_write
custom_write(name00, strings_in)

