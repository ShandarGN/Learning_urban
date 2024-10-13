# шапка задания
import sys
print ('Created by',sys.version)
print ('Дополнительное практическое задание по модулю 2')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*16)
# блок определений
dividers = []
div_unic = set()
pair = []
lst_pair = []
lst_unic_pair = set()
all_pair = set()
result = ''
str_pair = ''
first_cell = 0
# Блок ввода исходного числа, ограничение от 3 до 20
while not int(first_cell) in range(3,21):
    first_cell= input("Введите выпавшее число: ")
first_cell = int(first_cell)
print("Число выпавшее на первой ячейке -", first_cell)
# Блок определения делителей, удаления повторяющихся и 1
for i in range(1,first_cell+1):
    if first_cell % i == 0:
        dividers.append(i)
div_unic = set(dividers)
div_unic.discard(1)
div_unic = list(div_unic)
# Блок нахождения пар, которые при сложении дадут делитель
for i in div_unic:
    for j in range(1,i):
        pair = [j,i-j]
        pair = sorted(pair)
        str_pair =  str(pair[0]) + str(pair[1])
        lst_pair.append(str_pair)
    lst_unic_pair = set(lst_pair)
    all_pair =  all_pair | lst_unic_pair
    lst_pair.clear()
all_pair = sorted(list(all_pair))
# Блок формирования и вывода результата
for i in all_pair:
    result = result + i
print ('Код для второй ячейки -',result)