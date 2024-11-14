# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашнее задание по теме "Зачем нужно наследование"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
#Блок описания классов
    # Класс animal
class animal:
    alive = True
    fed = False
    def __init__(self,name_an):
        self.name = name_an
        # Метод eat класса animal (входные данные - food)
    def eat(self, food):
            # Проверка принадлежности классу predator
        if isinstance(self,predator):
                # проверка принадлежности классу animal
            if isinstance(food,animal):
                self.fed = True
                print(f'{self.name} съел {food.name} и насытился (сытость = {self.fed})')
            else:
                self.alive = False
                print(f'{self.name} не ест {food.name} и умер от голода (жизнь = {self.alive})')
        else:
            if food.edible == True:
                self.fed = True
                print(f'{self.name} съел {food.name} и насытился (сытость = {self.fed})')
            else:
                self.alive = False
                print(f'{self.name} не стал есть {food.name} и умер от голода (жизнь = {self.alive})')
    # Класс plant
class plant:
    edible = False
    def __init__(self,name_pl, edible_pl= False):
        self.name = name_pl
        self.edible = edible_pl
    # Прочие классы с указанием наследования
class mammal(animal):
    pass

class predator(animal):
    pass

class flower(plant):
    pass

class fruit(plant):
    pass
# Блок исходный данных
pl00 = fruit('Яблоко',True)
pl01 = plant('Крапива')
mm00 = mammal('Заяц')
pr00 = predator('Волк')
print(f'Имя растения: {pl00.name}, съедобное: {pl00.edible}, тип данных: {type(pl00)}, родительский класс : {type(pl00).__bases__} ')
print(f'Имя растения: {pl01.name}, съедобное: {pl01.edible}, тип данных: {type(pl01)}, родительский класс : {type(pl01).__bases__}')
print(f'Имя животного: {mm00.name}, живое: {mm00.alive}, сытое: {mm00.fed}, тип данных: {type(mm00)}, родительский класс : {type(mm00).__bases__}')
print(f'Имя животного: {pr00.name}, живое: {pr00.alive}, сытое: {pr00.fed}, тип данных: {type(pr00)}, родительский класс : {type(pr00).__bases__}')
print ('-'*20)
# Блок реализации метода eat разными классами и с различными данными
mm00.eat(pl00)
mm00.eat(pl01)
pr00.eat(pl00)
pr00.eat(mm00)
pr00.eat(pl01)
