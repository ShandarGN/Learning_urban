# Импорт необходимых библиотек
import threading
import time
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Создание потоков"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
    # Набор файлов и количества выводимых слов
        # Одним потоком
dict_input_0 = {'simple10.txt' : 10, 'simple11.txt' : 30, 'simple12.txt' : 200, 'simple13.txt' : 100}
        # Для нескольких потоков
dict_input_1 = {'simple20.txt' : 10, 'simple21.txt' : 30, 'simple22.txt' : 200, 'simple23.txt' : 100}
    # Пустой словарь потоков
dict_thrd = {}
# Описание рабочей функции wite_words (вход - словарь параметров и файл для чтения)
def wite_words(dict_input, file_name):
    with open(file_name, "r") as file_in:
        for j, k in dict_input.items():
            with open(j, "a") as file_out:
                print(f'Работа с файлом: {j}')
                print(f'Текущие потоки: {threading.enumerate()}')
                file_in.seek(0)
                for i in range(k):
                    read_char, word_in = '', ''
                    while read_char != ' ' and read_char != '\n' :
                        read_char = file_in.read(1)
                        word_in = word_in + read_char
                    word_in = word_in.rstrip()
                    word_in = word_in.replace('\n', '')
                    file_out.write(word_in)
                    print(f'Запись слова № {i} - {word_in}')
                    time.sleep(0.1)
                print(f'Завершилась запись в файл: {j}')
                print(f'Текущие потоки: {threading.enumerate()}')
# Начальная (start_thrd_main) и конечная (end_thrd_main) точки для расчета времени работы одним потоком
start_thrd_main = time.time()
# Запуск функции одним потоком
wite_words(dict_input_0, 'input_txt.txt')
end_thrd_main = time.time()
# Расчет и вывод времени выполнения
dlit_thrd_main = round(end_thrd_main - start_thrd_main, 2)
print('Время работы варианта с одним потоком:')
print(dlit_thrd_main)
print('Запуск функции несколькими потоками')
# Заполнение словаря потоков
for i , j in dict_input_1.items():
    thrd_name = f'thread0{i[7:8]}'
    dict_thrd[thrd_name] = threading.Thread(target = wite_words, args = ({i:j}, 'input_txt.txt', ))
# Вывод словаря потоков
print('Список используемых потоков:')
print(dict_thrd)
# Начальная (start_thrd_main) и конечная (end_thrd_main) точки для расчета времени работы c несколькими потоками
start_thrd_main_4 = time.time()
# Запуск функции разными потоками с приостановкой основного
dict_thrd['thread00'].start()
dict_thrd['thread01'].start()
dict_thrd['thread02'].start()
dict_thrd['thread03'].start()
dict_thrd['thread00'].join()
dict_thrd['thread01'].join()
dict_thrd['thread02'].join()
dict_thrd['thread03'].join()
# Расчет и вывод времени выполнения
end_thrd_main_4 = time.time()
dlit_thrd_main_4 = round(end_thrd_main_4 - start_thrd_main_4, 2)
print('Время работы варианта несколких потоков:')
print(dlit_thrd_main)
