# Импорт необходимых библиотек
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Генераторы"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Описание генератора подпоследовательностей переданной строки.
def all_variants(text):
    # Перебор номеров позиций из строки text
    for i in range(0, len(text)):
        # Перебор номеров от текущей позиции до конца строки text
        for j in range(i, len(text)):
            # Вычисление опорной точки для расчета среза
            point = len(text) - j - 1
            # Полученеи среза на основе опорной точки и номера позици
            yield text[point: point + i + 1]
# Исходные данные
gen_dict = {}
st = 'Привет!'
lst_st = ['Привет!', 'Абракадабра', 'Сезам']
# Создание одиночного генератора
gen_st = all_variants(st)
# Использование генератора и вывод данных
print(f'Генератор {gen_st} на основе строки {st}')
for i in gen_st:
    print(i)
print('-' * 20)
# Заполнение словаря генераторов
for i in lst_st:
    gen_name = f'Gen{lst_st.index(i)}'
    gen_dict[gen_name] = all_variants(i)
# Использование генераторов из словаря
for i in gen_dict.items():
    # Позиция из номера в ключе словаря gen_dict для вывода исходной строки из lst_st
    pos = int(i[0][3:len(i[0])])
    # Использование генераторов и вывод данных
    print(f'Генератор {i[0]}, id {i[1]}, на основе строки: {lst_st[pos]}')
    for j in i[1]:
        print(j)
    print('-' * 20)










