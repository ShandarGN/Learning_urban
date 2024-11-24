# Импорт необходимых библиотек
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Оператор "with"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
file_list = ['file_00.txt', 'file_01.txt', 'file_02.txt',]
lst_repl = [',', '.', '=', '!', '?', ';', ':', ' - ' ]
test_find = 'дед'
test_count = 'ванька'
"""
Функция удаления знаков препинания и конца строки, список удаляемого в lst_repl, 
Входные данные строка, выходные строка после обработки
"""
def repl(str_repl):
    global lst_repl
    str_repl = str_repl.replace('\n', ' ')
    for i in lst_repl:
         str_repl = str_repl.replace(i,'')
    return str_repl
# Класс WordsFinder, список имён файлов для поиска, в работе список находится в file_list
class WordsFinder:
    def __init__(self, list_names):
        self.file_names = tuple(list_names)
    # Функция преобразования содержимого файлов из file_list в список слов, выходные данные словарь: файл = список слов
    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8-sig') as file:
                str_j = ''
                for j in file:
                    str_j = str_j + repl(j.lower())
                all_words[i] = str_j.split()
        return all_words
    # Функция поиска слова, входные данные - искомое слово, выходные словарь: файл = первое вхождение
    def file_find(self, word):
        res_find = {}
        for i in self.get_all_words().items():
             if i[1].count(word.lower()) != 0:
                 res_find[i[0]] = i[1].index(word)
        return res_find
    # Функция подчета количества вхождения слова, входные данные - искомое слово, выходные словарь: файл = количество
    def file_count(self, word):
        res_count = {}
        for i in self.get_all_words().items():
             if i[1].count(word.lower()) != 0:
                 res_count[i[0]] = i[1].count(word.lower())
        return res_count
# Создание объекта для работы
WF = WordsFinder(file_list)
# Выходные данные
print('Примечание - отсчет ведется с нуля')
print('Список файлов: ', WF.file_names)
print('Файлы с содержимым в виде списка слов: ', WF.get_all_words())
print(f'Результат поиска слова "{test_find}" (файл и первая позиция): {WF.file_find(test_find)}')
print(f'Количество вхождения слова "{test_count}" (файл и количество): {WF.file_count(test_count)}')

