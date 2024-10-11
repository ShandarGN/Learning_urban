import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"')
print ('-'*20)
# Исходные данные и переменные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('Исходный список чисел -',numbers)
primes = [] # Пустой список для простых чисел
not_primes = [] # Пустой список для составных чисел
quantity_delitel = 0 # Количество делителей
# Выполняемая часть программы
for i in numbers: # Цикл по всем числам
    quantity_delitel = 0 # Обнуление счетчика делителей
    for j in numbers: # Перебор делителей
        if i % j == 0: # Если число делится на делитель без остатка
            quantity_delitel += 1 # Увеличиваем счетчик делителей
    if quantity_delitel == 2: # Если число делителей равно 2
        primes.append(i) # Добавляем число в список простых чисел
    elif quantity_delitel > 2: # Если число делителей больше 2
        not_primes.append(i) # Добавляем число в список составных чисел
    else: # Если число делителей равно 1
        pass # Пропускаем число 
# Вывод результатов
print('Простые числа -',primes) 
print('Составные числа -',not_primes)
