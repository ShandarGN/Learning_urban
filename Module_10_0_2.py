# Импорт необходимых библиотек
import threading
import time
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Потоки на классах"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
dict_enemy = {'Варвары' : 100, 'Сарацины' : 125, 'Разбойники' : 75 , 'Инопланетяне' : True}
dict_knight = {'Ланселот' : 20, 'Роланд' : 18, 'Эль Сид' : 17}
dict_thread = {}
# вывод исходных данных
print(dict_enemy)
print(dict_knight)
print('-' * 20)
# Описание класса потоков Knight (наследуется от threading.Thread, принимает параметры name и STR)
class Knight(threading.Thread):
    # Инициализация
    def __init__(self, name, STR):
        threading.Thread.__init__(self)
        # Проверки данных инициализации
        if type(name) == str:
            self.name = name
        else:
            print(f'Не строковые данные {name} не подходят для имени')
        if type(STR) == int and STR > 0:
            self.STR = STR
        else:
            print(f'Данные {STR} не подходят для Силы Рыцаря')
    # Метод Run (запуск)
    def run(self):
        for i, j in dict_enemy.items():
            # Проверка типа данных и изменение параметра enemy на STR потока с выводом результатов
            if type(j) in [int, float]:
                print(f'Рыцарь {self.name} на вас напали {i} числом {j} бойц.')
                battle = 0
                while j > self.STR:
                    time.sleep(1)
                    j -= self.STR
                    battle += 1
                    print(f'{self.name} сражается {battle} дн., осталось {j} бойц.')
                if j:
                    print(f'{i} испугались {self.name} и бежали через {battle} дн. битвы')
                    print(f'{self.name} одержал победу')
                    print('-' * 20)
                else:
                    print(f'{self.name} одержал победу спустя {battle} дн.!')
                    print('-' * 20)
            else:
                print(f'Врагов с такими параметрами {j} не бывает')
# Создание словаря потоков
for i , j in dict_knight.items():
    dict_thread[i] = Knight(i, j)
# Вывод словаря потоков
print(dict_thread)
print('-' * 20)
# Запуск потоков из словаря потоков
for i, j in dict_thread.items():
    print(f'Сражения рыцаря {i}')
    j.start()
    j.join()
    print('-'*20)
print('Все битвы закончились!')



