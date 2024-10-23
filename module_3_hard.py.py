# Шапка работы
import sys
print ('Created by',sys.version)
print ('Дополнительное практическое задание по модулю - 3')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Блок исходных данных и определения переменных
test = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
sum_n_l = 0
# Определение функции разбора сложного элемента
def razbor(obj_in):
    # Список участвующих в расчете классов
    use_class = (list,tuple,set,dict,str,int)
    # Список классов-коллекций
    coll_class = (list,tuple,set)
    global sum_n_l
    for i in obj_in:
        if isinstance(i,use_class):
            if isinstance(i,coll_class):
                razbor(i)
            elif isinstance(i,dict):
                i = i.items()
                razbor(i)
            else:
                if isinstance(i,str):
                    sum_n_l = sum_n_l + len(i)
                else:
                    sum_n_l = sum_n_l + i
        else:
            pass
    return sum_n_l
# Проверка
if razbor(test) == 0:
    print(f'Переданы пустые данные или только необрабатываемые объекты')
else:
    print(f'Сумма чисел и длин элементов равна: {sum_n_l}')