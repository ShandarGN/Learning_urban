# Импорт необходимых библиотек при запуске файла
"""
Для работы использованы измененные файлы для предыдущих заданий с необходимыми тестами
Управление пропуском тестов осуществляется изменением словарей dict_TournamentTest и dict_RunnerTest.
Сами файлы не измененны (отключено отображение шапки задания), наборы и результаты тестов сохранены.
"""
if __name__ == '__main__':
    import sys
    import unittest
    import Module_12_0_1 # Модуль с RunnerTest
    import Module_12_0_2 # Модуль с TournamentTest
# Шапка работы
    print ('Created by',sys.version)
    print ('Домашнее задание по теме "Систематизация и пропуск тестов".')
    print ('Студент Анисимов Алексей Юрьевич')
    print ('-'*20)
# Блок управления тестами
dict_TournamentTest = {'test_run_01': False, 'test_run_02': False, 'test_run_03': False, 'test_run_04': False, 'all': False}
dict_RunnerTest = {'test_walk': False, 'test_run': False, 'test_challenge': False, 'all': False}
if __name__ == '__main__':
    # Создание основного test_suit-а
    main_test = unittest.TestSuite()
    # Загрузка в него набота тестов RunnerTest и TournamentTest
    main_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_0_1.RunnerTest))
    main_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_0_2.TournamentTest))
    # Создание текстового Runnera тестов
    runner = unittest.TextTestRunner(verbosity=2)
    # Запуск Runnera тестов
    runner.run(main_test)
