# Импорт необходимых библиотек
from random import random
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Создание функций на лету"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
frst = 'Мама мыла раму'
scnd = 'Рамена мало было'
# Лямбда функция совпадения символов
sovp = lambda x,y: x == y
# Вывод результатов и несравниваемого остатка
print(f'{list(map(sovp, frst, scnd))}, остаток (это разность строк): {[False]*abs(len(frst)-len(scnd))}')
# Функция get_advanced_writer записи в файл file_name, создает функцию записи
def get_advanced_writer(file_name):
    # Функция записи переданных данных data_set
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i))
    return write_everything
# Вывод результатов по Замыканию, для записи используется файл - test.txt
write = get_advanced_writer('test.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 'Кавабанга')
# Создание класса MysticBall, для создания функции через метод класса __call__
class MysticBall():
    def __init__(self, *words):
        self.words = words
    # Описание меода __call__
    def __call__(self):
        return self.words[int(random() * len(self.words))]
# Создание объекта класса MysticBall
MBtest = MysticBall('Да', 'Нет', 'Наверное', 'У меня лапки', 'Я вообще шар')
# Вывод результатов
print(MBtest())



