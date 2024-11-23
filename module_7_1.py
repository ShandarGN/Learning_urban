# Шапка работы
import sys
print('Created by',sys.version)
print('Домашнее задание по теме "Режимы открытия файлов"')
print('Студент Анисимов Алексей Юрьевич')
print('-'*20)
# Исходные данные
var_product = {}
lst_name_prod = ['Apple','Melted milk','Schnitzel']
lst_weigth_prod = [1.5,1,0.4]
lst_category_prod = ['Fruit','Milk','Meаt']
# Описание используемых классов
    # Класс product (Продукты)
class product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
        # Метод __str__ (print)
    def __str__(self):
        return print(self.name, self.weight, self.category, sep = ', ')
    # Класс shop (магазин)
class shop():
    __file_name = 'products.txt'
        # Метод get_products (получение списка продуктов из __file_name)
    def get_products(self):
        file_in = open(shop.__file_name, 'r')
        str_in = file_in.read()
        file_in.close()
        return str_in
        # Метод add (добавление продуктов в __file_name)
    def add(self, prod):
        name_in_file = self.get_products()
        file_in = open(shop.__file_name, 'a')
        for i in prod.values():
            if i.name not in name_in_file:
                print('Добавлен в список: ', end = '')
                i.__str__()
                file_in.write('\n')
                file_in.write(i.name)
            else:
                print('Есть в магазине: ', end = '')
                i.__str__()
        file_in.close()
# Заполненеие списка добавляемых продуктов
for i in range(0, len(lst_name_prod)):
    var_name = f'prod{i}'
    var_product[var_name] = product(lst_name_prod[i], lst_weigth_prod[i], lst_category_prod[i])
# Создание объекта shop и вывод его содержимого
main = shop()
print('В магазине есть продукты:')
print(main.get_products())
print('-'*20)
# Вывод списка для добавления
print('Список для добавления:')
for i in var_product.values():
     i.__str__()
print('-' * 20)
# Добавление продуктов
print('Добавление продуктов:')
main.add(var_product)
print('-' * 20)
# Вывод результатов добавления
print('Теперь в магазине есть продукты:')
print(main.get_products())