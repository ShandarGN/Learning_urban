import random
import sys
print ('Created by',sys.version)
print ('Домашнее задание по теме "Множественное наследование"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные, список названий координат
name_coord = ['x','y','z']
""" 
Функция check_mov (входные данные: start - начальная координата, coord - текущая, speed - скорость, возвращает
возвращает итоговую координату, если результат больше нуля, иначе координата None
"""
def check_mov(start, coord, speed):
    if start + coord * speed < 0:
        return None
    else:
        return start + coord * speed
# Описание классов
    # Класс animal:
class animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    # Методы класса animal
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
    def move(self, xyz):
        for i in range(0, 3):
            result = check_mov(self._cords[i], xyz[i], self.speed)
            if result:
                self._cords[i] = result
            else:
                print('Глубоко, не умеет плавать!')
    def get_cords(self):
        global name_coord
        print('Текущие координаты:')
        for i in range(0, 3):
            print(f'{name_coord[i]}:{self._cords[i]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            return 'Sorry, i am peaceful :)'
        else:
            return 'Be careful, i am attacking you 0_0'
    def speak(self):
        print(self.sound)
    # Класс bird наследует от animal
class bird(animal):
    beak = True
        # Методы класса bird
    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1,4)} eggs for you')
    # Класс aquatic_animal наследует от animal
class aquatic_animal(animal):
    _DEGREE_OF_DANGER = 3
        # методы класса aquatic_animal
    def __init__(self, speed):
        super().__init__(speed)
    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - abs(dz) * self.speed/2
    # Класс poisonous_animal наследует от animal
class poisonous_animal(animal):
    _DEGREE_OF_DANGER = 8
    # Класс duckbill наследует от poisonous_animal, bird, aquatic_animal
class duckbill(poisonous_animal, bird, aquatic_animal):
    sound = 'Click-click-click'
# Создание объекта класса duckbill
db = duckbill(10)
# Вывод данных
print(db.live)
print(db.beak)
print(db.attack())
db.speak()
db.move([1,2,3])
print(db._cords)
db.dive_in(6)
print(db._cords)
db.lay_eggs()
