# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Атрибуты и методы объекта"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
print('ЖК Горский, 18 этажей, этаж для перезда - 4')
print('Домик в деревне, 2 этажаб этаж для перезда - 10')
# Описание класса
class house:
    def __init__(self,name_in,number_of_floors_in):
        self.name = name_in
        self.number_of_floors = number_of_floors_in
# Метод класса house, проверка этажа переезда и этажности дома
    def go_to(self,new_floor):
        if type(new_floor) == int:
            if new_floor > self.number_of_floors:
                print(f'Этаж - {new_floor}, больше, чем высота дома "{self.name}", равная {self.number_of_floors}')
            elif new_floor < 1:
                print(f'Нулевой или отрицательный этаж')
            else:
                print(f'Этажи для переезда: {list(range(1,new_floor))}')
        else:
            print(f'Введено нечисловое или нецелое значение этажа - {type(new_floor)}')
# Создание объектов класса house
h1 = house('ЖК Горский', 18)
h2 = house('Домик в деревне', 2)
# Применение методов класса house
print(f'{h1.name}')
h1.go_to(5)
print(f'{h2.name}')
h2.go_to(10)


