# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
begin = ['Ivan','VAZ-Kalina', 93, 'Red']
new_colors = ['Pink','White']
new_owner = 'Dmitriy'
# Описание используемых классов
class vehicle():
    __COLOR_VARIANTS = ['Red','Black','Grey','White']
    # Методы класса vehicle
    def __init__(self,owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    def get_model(self):
          print(f'Модель: {self._vehicle__model}')
    def get_horsepower(self):
         print(f'Мощность: {self._vehicle__engine_power}')
    def get_color(self):
         print(f'Цвет: {self._vehicle__color}')
    def print_info(self):
        print('Список характеристик:')
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')
        print(f'Вместимость: {self._sedan__PASSENGERS_LIMIT}')
    def set_color(self,new_color):
        for i in self._vehicle__COLOR_VARIANTS:
            if new_color.lower() == i.lower():
                print(f'Сменить цвет на {new_color} можно')
                self._vehicle__color = new_color
                return
        print(f'Сменить цвет на {new_color} нельзя')

class sedan(vehicle):
    __PASSENGERS_LIMIT = 5
# Создание объекта
car00 = sedan(*begin)
# Проверка методов и вывод данных
print(f'Данные машины (вывод разными методами):')
car00.get_model()
car00.get_horsepower()
car00.get_color()
print(f'Владелец: {car00.owner}')
print(f'Вместимость: {car00._sedan__PASSENGERS_LIMIT}')

print('\nВывод одни методом:')
print('\nДо изменения:')
car00.print_info()

print(f'\nЗапрос на изменение цвета на {new_colors[0]} ')
car00.set_color(new_colors[0])
print(f'Запрос на изменение цвета на {new_colors[1]} ')
car00.set_color(new_colors[1])

print('\nПосле изменения:')
car00.print_info()
