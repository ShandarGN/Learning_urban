# Импорт необходимых библиотек
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Итераторы"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные наборы параметров
lst_par = [[0, 10, 1], [0, -10, -2], [-1, -10, 2], [5, 10, -3], [1, 5, 0], [1, 8, 3]]
dict_par = {}
# Вывод исходных параметров
print('Наборы параметров итераторов:')
for i in lst_par:
    print(f'Вариант {lst_par.index(i)+1} - начало: {i[0]}, конец: {i[1]}, шаг: {i[2]}')
print ('-'*20)
# Описание класса "Ошибка значений итератора"
class StepValueError(ValueError):
    def __init__(self, message, info):
        self.message = message
        self.info = info
# Описание класса "Итератор"
class Iterator():
    # Инициализация
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        # Проверка корректности введенных данных
        if self.step == 0:
            raise StepValueError(f'Ошибка шага', self.step )
        elif self.step > 0 and self.start + self.step > self.stop:
            raise StepValueError(f'Ошибка начала, конца и шага', (self.start, self.stop, self.step))
        if self.step < 0 and self.start + self.step < self.stop:
            raise StepValueError(f'Ошибка начала, конца и шага', (self.start, self.stop, self.step))
    # Установка начального значения итератора
    def __iter__(self):
        self.pointer = self.start
        return self
    # Следующее значение итератора
    def __next__ (self):
        self.pointer = self.pointer + self.step
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration()
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration()
# Создание итератора с числом наборов переданных значений
main_it = Iterator(0, len(lst_par), 1)
# Генерация итераторов на основе переданных значений
for i in main_it:
    par_name = f'iterator{main_it.pointer}'
    print(f'Создание итератора {par_name}')
    # Обработка ошибок создания итераторов
    try:
        dict_par[par_name] = Iterator(lst_par[main_it.pointer-1][0], lst_par[main_it.pointer-1][1],
            lst_par[main_it.pointer-1][2])
    except StepValueError as err:
        print(f'{err.message} -  {err.info}')
    else:
        print(True)
# вывод созданных итераторов
print ('-'*20)
for i, j in dict_par.items():
    print(f'Итератор - {i}')
    print(f'Начало: {j.start}, конец: {j.stop}, шаг: {j.step}')
    for k in j:
        print(j.pointer)
    print('-' * 20)