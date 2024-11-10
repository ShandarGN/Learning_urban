from datetime import date
import sys

# Шапка работы
print ('Created by',sys.version)
print ('Задача "История строительства"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)

# Исходные данные
print('ЖК Эльбрус, 10 этажей, создан: 2020-12-12')
print('ЖК Акация, 20 этажей, создан: 2021-05-21')
print('ЖК Эльбрус, 20 этажей, создан: 2024-01-15')
name_house = ['ЖК Эльбрус','ЖК Акация','ЖК Матрёшки']
floor_house = [10,20,20]
date_sozd = ['2020-12-12','2021-05-21','2024-01-15']
print('-'*20)

# Описание класса
class house:
    houses_history = {}

    def __new__(cls,*args):
        cls.houses_history[args[0]]=''
        return object.__new__(cls)

    def __init__(self, *args):
        self.name = args[0]
        self.number_of_floors = args[1]
        self.date_sozd = args[2]
        print(f'Создание объекта - {self.name}')
        print(f'История созданных объектов c датой удаления \n {self.houses_history}\n')

    def __del__(self):
        house.houses_history[self.name]=str(date.today())  
        print(f'Удаление объекта - {self.name}')      
        print(f'{self.name} снесён {date.today()}, но он останется в истории')
        print(f'История созданных объектов c датой удаления \n {self.houses_history}\n')

# Создание объектов класса house
h1 = house(name_house[0], floor_house[0], date_sozd[0])
h2 = house(name_house[1], floor_house[1], date_sozd[1])
h3 = house(name_house[2], floor_house[2], date_sozd[2])

# Удаление обьектов класса house
del h2
del h3