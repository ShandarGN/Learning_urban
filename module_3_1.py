# шапка задания
import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Пространство имён"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# блок определений и исходных данных
calls = 0
    # данные для первой функции, строки
fn01_str01 = 'hgРНщя697Gf'
fn01_str02 = 'Привет товарищ'
fn01_str03 = 'AbCdFgH'
fn01_str04 = 'До свидания'
    # данные для второй функции, строки и списки
fn02_str01 = 'АgtЩ'
fn02_str02 = 'abc'
fn02_lst01 = [123,'Привет',25.5968]
fn02_lst02 = ['abcdef','АВВГДЕ']
        # блок вывода исходных данных
print('Данные для первой функции (строки): ')
print(f'1: {fn01_str01} \n2: {fn01_str02} \n3: {fn01_str03} \n4: {fn01_str04}')
print('-'*20)
print('Данные для второй функции (строки)')
print(f'1: {fn02_str01} \n2: {fn02_str02}')
print('Данные для второй функции, списки')
print(f'1: {fn02_lst01} \n2: {fn02_lst02}')
print('-'*20)
# блок описания функций
    # функция 00 count_calls
def count_calls():
    global calls
    calls = calls + 1
    # функция 01 - string_info
def string_info(in_str_01 = ''):
    count_calls()
    tuple_str = (str(len(in_str_01)), in_str_01.upper(), in_str_01.lower())
    return tuple_str
    # функция 02 - is_contains
def is_contains(in_str_02 = '',in_list_02 = []):
    count_calls()
    result = False
    in_str_02 = in_str_02.upper()
    in_list_02 = str(in_list_02).upper()
    if in_list_02.find(in_str_02) != -1:
        result = True
    return result
# блок расчетов и вывода результатов
print ('Результаты первой функции, кортежи -')
print('1:',string_info(fn01_str01))
print('2:',string_info(fn01_str02))
print('3:',string_info(fn01_str03))
print('4:',string_info(fn01_str04))
print ('Результаты второй функции, логические значения -')
print('1:',is_contains(fn02_str01,fn02_lst01))
print('2:',is_contains(fn02_str02,fn02_lst02))
print('Количество использований функций - ',calls)