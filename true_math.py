# Подключение библиотеки math для доступа к значению бесконечнеость (inf)
from math import inf
# Описание функции деления, при нуле возврат матмеатической бсконечности, при нечисловых значениях возврат None
def div(frst,scnd):
    # Допустимые классы числовых значений
    dop_class = (int,float)
    # Проверка данных на принадлежность числовым значениям
    if (type(frst) in dop_class)+(type(scnd) in dop_class) == 2:
        # Проверка делителя на 0
        if scnd == 0:
            return inf
        # Деление
        else:
            res = frst/scnd
            return res
    # Возврат None при передаче нечисловых значений
    elif (type(frst) in dop_class) + (type(scnd) in dop_class) < 2:
        return
