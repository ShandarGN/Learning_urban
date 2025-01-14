# Импорт необходимых библиотек
# import sys
import unittest
import pprint
# Подключение модуля с управляющим словарем
# https://github.com/ShandarGN/Learning_urban/blob/main/Mod_suite_12_3.py
import Mod_suite_12_3
# # Шапка работы
# print ('Created by',sys.version)
# print ('Домашнее задание по теме "Методы Юнит-тестирования"')
# print ('Студент Анисимов Алексей Юрьевич')
# print ('-'*20)
# Исходные данные
dict_runners = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
dict_runners_obj = {}
# Описание класса Runner
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
# Описание класса Tournament
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
    # Метод start класса Tournament (возвращает словарь - список участников и их место в турнире)
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers
# Описаник класса TournamentTest (тест класса Tournament)
class TournamentTest(unittest.TestCase):
    # Добавление атрибутов all_results к классу Tournament
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    # Заполнение списка dict_runners_obj (объекты класса Runner) для использования при тестировании класса Tournament
    def setUp(self):
        for i, j in dict_runners.items():
            dict_runners_obj[i]= Runner(i, j)
    # Первый тест класса Tournament и проверка его пропуска
    @unittest.skipIf(Mod_suite_12_3.dict_TournamentTest['test_run_01'] or Mod_suite_12_3.dict_TournamentTest['all'],
                     'test_run_01 - пропущен')
    def test_run_01(self):
        Tournament_tst = Tournament(90, dict_runners_obj['Усэйн'], dict_runners_obj['Ник'])
        self.all_results.update({'Test01': Tournament_tst.start()})
        # Проверка истинности условия для теста
        self.assertTrue(self.all_results['Test01'][2] == 'Ник')
    # Второй тест класса Tournament и проверка его пропуска
    @unittest.skipIf(Mod_suite_12_3.dict_TournamentTest['test_run_02'] or Mod_suite_12_3.dict_TournamentTest['all'],
                     'test_run_02 - пропущен')
    def test_run_02(self):
        Tournament_tst = Tournament(90, dict_runners_obj['Андрей'], dict_runners_obj['Ник'])
        self.all_results.update({'Test02': Tournament_tst.start()})
        # Проверка истинности условия для теста
        self.assertTrue(self.all_results['Test02'][2] == 'Ник')
    # Третий тест класса Tournament и проверка его пропуска
    @unittest.skipIf(Mod_suite_12_3.dict_TournamentTest['test_run_03'] or Mod_suite_12_3.dict_TournamentTest['all'],
                     'test_run_03 - пропущен')
    def test_run_03(self):
        Tournament_tst = Tournament(90, dict_runners_obj['Усэйн'], dict_runners_obj['Андрей'],
                                    dict_runners_obj['Ник'])
        self.all_results.update({'Test03': Tournament_tst.start()})
        # Проверка истинности условия для теста
        self.assertTrue(self.all_results['Test03'][3] == 'Ник')
    """
    Четвертый тест класса Tournament
    Данный тест добавлен для проверки логической ошибки в методе Tournament.start
    Суть ошибки - если дистанция меньше или равна скорости самого медленного спортсмена и он передан в метод первым,
    то он получит первое место. Причина - так как метод Runner.run и проверка заверешния забега проводятся для 
    каждого переданного бегуна в одном элементе цикла, то бегун может в этом элементе сразу закончить забег и станет 
    первым. Для проверки в тест переданы дистанция равная скорости самого медленного, он сам (Ник) и самый быстрый 
    бегун (Усэйн), если подходить с точки зрения логики, то Ник должен прийти вторым, но в результате метода 
    Tournament.start этого не произойдёт. 
    """
    @unittest.skipIf(Mod_suite_12_3.dict_TournamentTest['test_run_04'] or Mod_suite_12_3.dict_TournamentTest['all'],
                     'test_run_04 - пропущен')
    def test_run_04(self):
        Tournament_tst = Tournament(3, dict_runners_obj['Ник'], dict_runners_obj['Усэйн'])
        self.all_results.update({'Test04': Tournament_tst.start()})
        self.assertTrue(self.all_results['Test04'][2] == 'Ник')
    # Вывод атрибута all_results (результаты тестов)
    @classmethod
    def tearDownClass(cls):
        pprint.pprint(cls.all_results)
if __name__ == '__main__':
    unittest.main()
