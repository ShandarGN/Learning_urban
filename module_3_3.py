# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашнее задание по уроку "Распаковка позиционных параметров"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Часть 1
# Блок описания функции, заданы с параметры по умолчанию
def print_par(a=1,b='Текст',c=True):
    print(f'a = {a}, b = {b}, c = {c}')
# Варианты вывода функции с разным количеством и типом параметров
print_par()
print_par(125)
print_par(597,'Два параметра')
print_par(69874,'Три параметра',False)
print_par(c = [1,2,3])
print ('-'*20)
# Часть 2 Распаковка параметров
values_list = [659.875,45,'Homeland']
values_dict = {'a':458.251,'b':False,'c':'Человек'}
print_par(*values_list)
print_par(**values_dict)
print ('-'*20)
# Часть 3 Распаковка + отдельные параметры.
values_list_2 = ['Фабрика',6598.259]
print_par(*values_list_2, 542)
