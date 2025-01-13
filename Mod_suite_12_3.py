# Импорт необходимых библиотек
"""
Для работы использованы измененные файлы для предыдущих заданий с необходимыми тестами
Управление пропуском тестов осуществляется изменением словаря dict_tests в каждом файле.
Сами файлы не измененны, наборы и результаты тестов сохранены.
"""
import sys
import unittest
import Module_12_0_1 # Модуль с RunnerTest
import Module_12_0_2 # Модуль с TournamentTest
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Систематизация и пропуск тестов".')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Создание основного test_suit-а
main_test = unittest.TestSuite()
# Загрузка в него набота тестов RunnerTest и TournamentTest
main_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_0_1.RunnerTest))
main_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_0_2.TournamentTest))
# Создание текстового Runnera тестов
runner = unittest.TextTestRunner(verbosity=2)
# Запуск Runnera тестов
runner.run(main_test)