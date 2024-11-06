# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Специальные методы классов"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)

# Исходные данные
print('ЖК Горский, 18 этажей, этаж для перезда - 4')
print('Домик в деревне, 2 этажа, этаж для перезда - 10')
name_house = ['ЖК Горский','Домик в деревне']
floor_house = [18,2]
print('-'*20)

# Функция подбора окончания
def okonch(num):
    num = num % 10
    if num == 0:
        return ''
    elif num == 2 or num == 3 or num == 4:
        return 'а'
    else:
        return 'ей'

# Описание класса
class house:
    def __init__(self, name_in, number_of_floors_in):
        self.name = name_in
        self.number_of_floors = number_of_floors_in
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        print(f'В доме {self.name} имеется {self.number_of_floors} этаж{okonch(len(self))}')

# Создание объектов класса house
h1 = house(name_house[0], floor_house[0])
h2 = house(name_house[1], floor_house[1])

# Использование специальных (магических) методов
print(f'Количество этажей через метод __len__: {len(h1)}')
print(f'Описание через метод __str__:')
h1.__str__()
print('-'*20)
print(f'Количество этажей через метод __len__: {len(h2)}')
print(f'Описание через метод __str__:')
h2.__str__()









