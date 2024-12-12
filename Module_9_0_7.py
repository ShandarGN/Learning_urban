# Импорт необходимых библиотек
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Декораторы"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Описание декоратора is_prime
def is_prime(func):
    def in_prime(one, two, thr):
        num = func(one, two, thr)
        if type(num) == int:
            if num > 0:
                check_del = 0
                for i in range(1, num):
                    if num % i == 0:
                        check_del = check_del + 1
                        if check_del > 2:
                            return f'{num} - cоставное число'
                return f'{num} - простое число'
            else:
                return f'Введено неположительное число {num}'
        return f'Введены нечисловые параметры, введенные типы: {num}'
    return in_prime
# Применение декоратора is_prime к функции sum_three
@is_prime
    # Описание функции sum_three
def sum_three(one, two, thr):
        # Проверка валидности переданных данных
    types = list(map(type, [one, two, thr]))
    if types.count(int) + types.count(float) == 3:
        return one + two + thr
    else:
        return types
# Исходные данные
lst_par = [[10, 5, 8], [12, 6, 2], [-3, 8, -5], [-15, 8, -5], [True, 'S', 5]]
# Обработка данных и вывод результатов
for i in lst_par:
    print(f'Исходные данные: {i}')
    result = sum_three(*i)
    print(result)
    print ('-'*20)
