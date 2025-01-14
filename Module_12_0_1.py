# Импорт необходимых библиотек
# import sys
import unittest
import random
# Подключение модуля с управляющим словарем
# https://github.com/ShandarGN/Learning_urban/blob/main/Mod_suite_12_3.py
import Mod_suite_12_3
# # Шапка работы
# print ('Created by',sys.version)
# print ('Домашнее задание по теме "Простые Юнит-Тесты"')
# print ('Студент Анисимов Алексей Юрьевич')
# print ('-'*20)
# Описание функции генерации случайных имен, принимает длину имён
def rnd_name(dln):
    abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z')
    name = ''
    for i in range(dln):
       name = name + random.choice(abc)
    return name
# Задние длины случайных имен, количества тестируемых объектов и числа попыток
dln = 6
kol = 4
count_test = 10
# Описание тестируемого класса Runner
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0
    # Метод run
    def run(self):
        self.distance += 10
    # Метод walk
    def walk(self):
        self.distance += 5
    # Метод вывода имени объекта класса
    def __str__(self):
        return self.name
# Создание имен тестируемых объектов
runner_name = list(map(rnd_name, [dln for i in range(kol)]))
# Описание класса тестов
class RunnerTest(unittest.TestCase):
    count = count_test
    runner_list = []
    # Заполнение классового списка тестируемых объектов
    for i in runner_name:
        runner_list.append(Runner(i))
    # Тестирование метода walk
    @unittest.skipIf(Mod_suite_12_3.dict_RunnerTest['test_walk'] or Mod_suite_12_3.dict_RunnerTest['all'],
                     'test_walk - пропущен')
    def test_walk(self):
        for j in RunnerTest.runner_list:
            for i in range(RunnerTest.count):
                j.walk()
            self.assertEqual(j.distance, 50)
            j.distance = 0
    # Тестирование метода run
    @unittest.skipIf(Mod_suite_12_3.dict_RunnerTest['test_run'] or Mod_suite_12_3.dict_RunnerTest['all'],
                     'test_run - пропущен')
    def test_run(self):
        for j in RunnerTest.runner_list:
            for i in range(RunnerTest.count):
                j.run()
            self.assertEqual(j.distance, 100)
            j.distance = 0
    # Тестирование различий результатов методов walk и run
    @unittest.skipIf(Mod_suite_12_3.dict_RunnerTest['test_challenge'] or Mod_suite_12_3.dict_RunnerTest['all'],
                     'test_challenge - пропущен')
    def test_challenge(self):
        for j in range(kol//2):
            for i in range(RunnerTest.count):
                RunnerTest.runner_list[j * 2].run()
                RunnerTest.runner_list[j * 2 + 1].walk()
            self.assertNotEqual(RunnerTest.runner_list[j * 2].distance, RunnerTest.runner_list[j * 2 + 1].distance)
            RunnerTest.runner_list[j * 2].distance = 0
            RunnerTest.runner_list[j * 2 + 1].distance = 0

if __name__ == '__main__':
    unittest.main()
