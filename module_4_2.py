# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Пространство имен."')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
print('Глобальное пространство имён до пределения внешней функции: ',globals(),'\n')
# Определение внешней функции
def test_function():
    print('Простаранство имен test_function до вызова inner_function', locals(),'\n')
    # Определение внутренней функции
    def inner_function():
        print('Я в области видимости функции test_function','\n')
        print('Простаранство имен функции inner_function: ', locals(),'\n')
    # Вызов внутренней функции
    inner_function()
    print('Простаранство имен test_function после вызова inner_function', locals(),'\n')
# Вызов внешней функции
test_function()
print('Глобальное пространство имён после вызова test_function: ',globals(),'\n')
# Видим, что в глобальном пространстве имен нет имени inner_function, потому при вызове её извне получим ошибку
# Для вызова inner_function необходимо получить доступ к локальному пространству test_function из глобального
# Вызов внутренней функции с обработкой ошибки
try:
     inner_function()
except:
    print("Ошибка при вызове inner_function - NameError: name 'inner_function' is not define.")


