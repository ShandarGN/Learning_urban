# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Атрибуты и методы объекта"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
print('ЖК Горский, 18 этажей, этаж для перезда - 4')
print('Домик в деревне, 2 этажа, этаж для перезда - 10')
name_house = ['ЖК Горский','Домик в деревне']
floor_house = [18,2]
floor_go = [4,10]
print('-'*20)
# Описание класса
class house:
    def __init__(self,name_in,number_of_floors_in):
        self.name = name_in
        self.number_of_floors = number_of_floors_in
# Метод go_to класса house, проверка этажа переезда и этажности дома с непосредственным выводом результатов
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
# Метод go_to класса house, с формированием данных для функции вывода
    def go_to_1(self,new_floor):
        if type(new_floor) == int:
            if new_floor > self.number_of_floors:
                return -1, self.name, self.number_of_floors, new_floor
            elif new_floor < 1:
                return 0, self.name, self.number_of_floors, new_floor
            else:
                return list(range(1,new_floor+1)), self.name, self.number_of_floors,new_floor
        else:
            return None, self.name, self.number_of_floors,new_floor
# Описание функции вывода результатов
def pr_itog(lst_floor, name, number_of_floors, new_floor):
    if lst_floor != None:
        if lst_floor == -1:
            print(f'Этаж - {new_floor}, больше, чем высота дома "{name}", равная {number_of_floors}')
        elif lst_floor == 0:
            print(f'Нулевой или отрицательный этаж')
        else:
            print(f'Этажи для переезда: {lst_floor}')
    else:
        (f'Введено нечисловое или нецелое значение этажа')
# Создание объектов класса house
h1 = house(name_house[0], floor_house[0])
h2 = house(name_house[1], floor_house[1])
# Применение методов класса house
# Метод go_to - непосредственный вывод результатов методом
print ('Метод go_to')
print(f'{h1.name}')
h1.go_to(5)
print(f'{h2.name}')
h2.go_to(10)
print('-'*20)
# Метод go_to_1 - формирование данных для функции вывода и передача их в функцию
print ('Метод go_to_1')
pr_itog(*h1.go_to_1(floor_go[0]))
pr_itog(*h2.go_to_1(floor_go[1]))
