# Импорт необходимых библиотек
import sys
import unittest
import logging
# Исходные данные
    # Словарь параметров тестируемых объектов
runners = {'Вася': 10, 'Илья': 5, 'Арсен': 11, 'Игнат' : -3, True: 5}
    # Количество итераций в тестах run и walk
count_test = 10
    # Словарь объектов для тестирования
main_dict_runners_obj = {}
    # Словарь управляющий пропуском тестов
dict_tests_runners = {'test_walk': False, 'test_run': False, 'test_challenge': False, 'all': False}
# Подключение логирования
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8', format='%(asctime)s | %(levelname)s | %(message)s')
# Шапка работы записанная в лог-файл
logging.info(f'Created by,{sys.version}')
logging.info('Домашнее задание по теме "Логирование"')
logging.info('Студент Анисимов Алексей Юрьевич')
logging.info(('-'*20))
# Описание класса Runner
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, {speed} для бегуна {self.name}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
# Описание класса тестов RunnerTest
class RunnerTest(unittest.TestCase):
    # Словарь входных данных и число итераций в тестах
    dist_res_test_runner = {'walk': {'Вася': 100, 'Илья': 50, 'Арсен': 110}, 'run': {'Вася': 200, 'Илья': 100, 'Арсен': 220}}
    count = count_test
    # Заполнение списка тестируемых объектов
    """
    Так как выбранный вариант выполнения предполагает передачу для тестирования уже созданных объектов, то именно этот 
    процесс будет в основной части логирования.
    """
    for i,j in runners.items():
        try:
            main_dict_runners_obj[i] = Runner(i, j)
            logging.info(f'Объект Runner {i} создан успешно')
        except ValueError as VErr:
            logging.warning(f'Неверная скорость для Runner. Ошибка: {VErr}')
        except TypeError as TErr:
            logging.warning(f'Неверный тип данных для объекта Runner. Ошибка: {TErr}')
    # Тестирование метода walk с использованием логирования хода тестов
    try:
        # Проверка (try) самого теста
        @unittest.skipIf(dict_tests_runners['test_walk'] or dict_tests_runners['all'], 'test_walk - пропущен')
        def test_walk(self):
            for j in main_dict_runners_obj.values():
            # Проверка (try) тестирования переданного в тест объекта
                try:
                    for i in range(RunnerTest.count):
                        j.walk()
                    self.assertEqual(j.distance, self.dist_res_test_runner['walk'][j.name])
                    logging.info(f'Объект {j} протестирован test_walk')
                    j.distance = 0
                except:
                    logging.warning(f'test_walk для объекта {j} не выполнен')
            logging.info(f'Тест - test_walk выполнен успешно')
    except:
        logging.warning('Тест - test_walk не выполнен')
    # Тестирование метода run с использованием логирования хода тестов
        # Проверка (try) самого теста
    try:
        @unittest.skipIf(dict_tests_runners['test_run'] or dict_tests_runners['all'], 'test_run - пропущен')
        def test_run(self):
            for j in main_dict_runners_obj.values():
                # Проверка (try) тестирования переданного в тест объекта
                try:
                    for i in range(RunnerTest.count):
                        j.run()
                    self.assertEqual(j.distance, self.dist_res_test_runner['run'][j.name])
                    logging.info(f'Объект {j} протестирован test_run')
                    j.distance = 0
                except:
                    logging.warning(f'test_run для объекта {j} не выполнен')
            logging.info(f'test_run выполнен успешно')
    except:
        logging.warning('test_run не выполнен')
    # Тестирование различий результатов методов walk и run
        # Проверка (try) самого теста
    try:
        @unittest.skipIf(dict_tests_runners['test_challenge'] or dict_tests_runners['all'], 'test_challenge - пропущен')
        def test_challenge(self):
            for j in main_dict_runners_obj.values():
                # Проверка (try) тестирования переданного в тест объекта
                try:
                    for i in range(RunnerTest.count):
                        j.run()
                    RTD_run = j.distance
                    j.distance = 0
                    for i in range(RunnerTest.count):
                        j.walk()
                    RTD_walk = j.distance
                    j.distance = 0
                    self.assertNotEqual(RTD_run, RTD_walk)
                    logging.info(f'Объект {j} протестирован test_challenge')
                except:
                    logging.warning(f'test_challenge для объекта {j} не выполнен')
            logging.info(f'test_challenge выполнен успешно')
    except:
        logging.warning('test_challenge не выполнен')

if __name__ == '__main__':
    unittest.main()

