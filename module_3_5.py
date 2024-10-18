# Шапка работы
import sys
print ('Created by',sys.version)
print ('Самостоятельная работа по уроку "Рекурсия"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Блок определения глобальных переменных
mult_dig = 1
# Блок определения функции
def get_multiplied_digits(number):
    # Блок определения переменных функции get_multiplied_digits
    str_number = str(number)
    # Срез первого знака
    first = str_number[0]
    # Проверка однозначности переданного числа
        # Многозначное число
    if len(str_number) > 1:
        global mult_dig
        # Умножение первого знака на глобальную переменную
        mult_dig = mult_dig * int(first)
        # Возврат функцией среза со второй позиции
        return get_multiplied_digits(int(str_number[1:]))
        # Однозначное число
    else:
        # Поверка состояния глобальное переменной, для определения факта первого вызова функции
            # Первый вызов
        if mult_dig == 1:
            print(f'Введено однозначное число: {first}')
            return ''
            # Второй и более вызовы
        else:
            # Умножение первого знака на глобальную переменную
            return mult_dig*int(first)
# Вызов функции и печать результатов
print(get_multiplied_digits(int(input('Введите число: '))))
