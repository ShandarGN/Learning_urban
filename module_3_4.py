# Шапка работы
import sys
print ('Created by',sys.version)
print ('Самостоятельная работа по уроку "Произвольное число параметров"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Блок определения переменных
words = ['POST','Most','gRim','bOOk','hoST','trAst','FAsT','cooK','lOOk','triMinG','CaSTing','CasTLe']
# Блок описания функции
def single_root_words(root_word='',*other_words):
    same_words = []
    if root_word in '': # Проверка ввода данных
        return 'Не введено слово для поиска!'
    else:
        for i in other_words: # Поиск и заполнение списка результатов
            if root_word.lower() in i.lower():
                same_words.append(i)
        if not same_words:
            same_words = ['Совпадений нет!']
# Вывод результатов поиска
    return print('Поиск слов содержащих слово:', root_word, '\nв списке слов:', *other_words,'\nитог:', *same_words)
# Вызов функции
single_root_words(str(input('Введите слово для поиска:')),*words)
