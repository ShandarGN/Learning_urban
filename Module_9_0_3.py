# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашнее задание по теме "Генераторные сборки"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
frst = ['Strings', 'Student', 'Computers']
scnd = ['Строка', 'Урбан', 'Компьютер']
# Выполнение работы функциональным методом
    # Функция проверки корректности данных
def obrab(frst, scnd):
    return [i for i in frst if type(i) != str], [i for i in scnd if type(i) != str], len(frst) == len(scnd), frst, scnd
    # Функция выполнения заданий
def work(check):
        # Обработка результатов проверки
    if check[0]:
        print(f'В первом списке нестроковые параметны: {check[0]}')
        if check[1]:
            print(f'Во втором списке нестроковые параметны {check[1]}')
    elif not check[2]:
        print('У переданных списков неравная длина')
    else:
        # Задание 1
        frst_res = [abs(len(i[0]) - len(i[1])) for i in zip(check[3], check[4]) if len(i[0]) != len(i[1])]
        print('Разница длин строк из переданных списков, если их длины соответствующих строк не равны')
        print(frst_res)
        print('В виде словаря результатов (модуль результата):')
        frth_res = {i[0] + ' - ' + i[1]: abs(len(i[0]) - len(i[1])) for i in zip(check[3], check[4])
            if len(i[0]) != len(i[1])}
        print(frth_res)
        # Задание 2
        scnd_res = [i == j for i in check[3] for j in check[4] if check[3].index(i) == check[4].index(j)]
        print('Результат сравнения длин строк на одинаковых позициях из переданных списков')
        print(scnd_res)
        print('В виде словаря результатов:')
        thrd_res = {i + ' == ' + j: i == j for i in check[3] for j in check[4] if check[3].index(i)
            == check[4].index(j)}
        print(thrd_res)
# Применение функции "Выполнение заданий"
work(obrab(frst, scnd))
print('-'*20)
# Выполнение работы объектным методом
    # Описание класса "Работа"
class works_obj():
    def __init__(self, frst, scnd):
        self.frst = frst
        self.scnd = scnd
    # Описание классового метода "Проверка объекта"
    def obrab_obj(self):
        return ([i for i in self.frst if type(i) != str], [i for i in self.scnd if type(i) != str],
            len(self.frst) == len(self.scnd))
    # Описание классового метода "Выполнение заданий"
    def zadan_obj(self):
        # Обработка результатов проверки
        check = self.obrab_obj()
        if check[0]:
            print(f'В первом списке нестроковые параметны: {check[0]}')
            if check[1]:
                print(f'Во втором списке нестроковые параметны {check[1]}')
        elif not check[2]:
            print('У переданных списков неравная длина')
        else:
            # Задание 1
            frst_res = [abs(len(i[0]) - len(i[1])) for i in zip(self.frst, self.scnd) if len(i[0]) != len(i[1])]
            print('Разница длин строк из переданных списков, если их длины соответствующих строк не равны')
            print(frst_res)
            print('В виде словаря результатов (модуль результата):')
            frth_res = {i[0] + ' - ' + i[1]: abs(len(i[0]) - len(i[1])) for i in zip(self.frst, self.scnd)
                        if len(i[0]) != len(i[1])}
            print(frth_res)
            # Задание 2
            scnd_res = [i == j for i in self.frst for j in self.scnd if self.frst.index(i) == self.scnd.index(j)]
            print('Результат сравнения длин строк на одинаковых позициях из переданных списков')
            print(scnd_res)
            print('В виде словаря результатов:')
            thrd_res = {i + ' == ' + j: i == j for i in self.frst for j in self.scnd if self.frst.index(i)
                        == self.scnd.index(j)}
            print(thrd_res)
# Создание объекта класса "Работа"
w9_0_3 = works_obj(frst, scnd)
# Применение классового медота "Выполнение заданий"
w9_0_3.zadan_obj()






