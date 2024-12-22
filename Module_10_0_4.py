# Импорт необходимых библиотек
import threading
import time
from queue import Queue
import random
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Очереди для обмена данными между потоками."')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
kol_table = 3
dict_table = {}
dict_quest = {}
lst_name = ['Ivan Fool', 'Vasilisa Beauty', 'Little John', 'Robin Good', 'Alladin']
# Описание класса table (входные - Номер и Гость, по умолчанию None)
class table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest
# Описание класса guest наследуется от threading.Thread (входные - Имя)
class guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    # Метод run - ожидание в диапазоне от 3 до 10 секунд
    def run(self):
        time.sleep(random.randint(3, 10))
# Описание класса cafe (входые - Очередь (класс Queue()) и список столиков
class cafe():
    def __init__(self,args):
        self.queue = Queue()
        self.tables = [*args]
    # Метод guest_arrival (входные - набор Гостей)
    def guest_arrival(self, guest):
        # Перебор Гостей
        for i in guest:
            izm = False
            # Перебор столиков
            for j in self.tables:
                # Размещенеи госта яна путом столик и запуск его потока
                if j.guest == None:
                    j.guest = i
                    print(f'{i.name} сел(-а) за стол номер {j.number}')
                    i.start()
                    izm = True
                    break
            if izm == False:
                # Перемещение Гостя в очередь, при отсутствии пустых столиков
                self.queue.put(i)
                print(f'Нет столика для посетителя {i.name}, он перемещен в очередь {self.queue}')
                print(f'Текущий размер очереди {self.queue.qsize()}')
    # Метод discuss_guests
    def discuss_guests(self):
        # Пока очередь не пуста или хоть один столик занят
        while not self.queue.empty() or [i.guest for i in self.tables if i.guest] != []:
            # Перебор столиков
            for i in self.tables:
                # Проверка наличия Гостя за Столиком
                if i.guest:
                    # Проверка существования потока Гостя (Гость еще за столиком)
                    if not i.guest.is_alive():
                        print(f'{i.guest.name} покушал(-а) и ушёл(ушла)')
                        # Освобождение столика, если поток Гостя завершён
                        i.guest = None
                        print(f'Столик {i.number} свободен')
                else:
                    # Проверка наличия Гостей в очереди
                    if not self.queue.empty():
                        # Перевод Гостя из очереди за столик и запуск его потока
                        i.guest = self.queue.get()
                        print(f'{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
                        print(f'Текущий размер очереди {self.queue.qsize()}')
                        i.guest.start()
                        i.guest.join()
            time.sleep(1)
# Заполнение словаря Столиков
for i in range(kol_table):
    var_table = f'tbl_{i}'
    dict_table[var_table] = table(f'n_{i}')
# Заполнение словаря Гостей
for i in lst_name:
    var_quest = f'q_{i}'
    dict_quest[var_quest] = guest(var_quest)
# Создане объектса класса  afe
elefant = cafe(dict_table.values())
# Применение метода guest_arrival к словарю Гостей
elefant.guest_arrival([i for i in dict_quest.values()])
# Резульата применения метода guest_arrival
print('00',[i.guest for i in elefant.tables])
# Применение метода discuss_guests
elefant.discuss_guests()
# Результат применения метода discuss_guests
print('01',[i.guest for i in elefant.tables])





