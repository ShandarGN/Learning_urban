# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашнее задание по теме "Создание исключений"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходеные данные
dict_car = {'0000' : None}
lst_name = ['Lada', 'BMW', 'Honda', 'Mazda', 'Mersedes', 'Opel', 'Kamaz']
lst_VIN = [123456, 956.859, 359435, 15090435, 190435, 659841, 458961]
lst_num = ['654321', '159784', 659848, '659848', 'LTR659848', '596', 'КС5596']
# Описание классов исключений
    # Ошибка в VIN
class  IncorrectVinNumber(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info
    # Ошибка в номере
class IncorrectCarNumbers(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info
# Описание класса Car, входные данные - модель, VIN и номер.
class car():
    def __init__(self, model, vin, number):
        self.model = model
        # Заполнение поля VIN по результатам проверки VIN на валидность
        if self._car__is_valid_vin(vin):
            self.__vin = vin
        # Заполнение поля номер по результатам проверки его на валидность
        if self._car__is_valid_numbers(number):
            self.__number = number
# Функция проверки VIN на валидность
    def __is_valid_vin(self, vin):
    # Проверка типа VIN
        if not(isinstance(vin, int)):
            raise IncorrectVinNumber(f'Введён некорректный тип VIN: {type(vin)}', vin)
    # Проверка диапазона вин от 0 до 1000000
        if vin < 0 or vin > 10000000:
            raise IncorrectVinNumber(f'Неверный диапазон для VIN', vin)
        else:
            return True
# Функция проверки валидности номера
    def  __is_valid_numbers(self, number):
    # Проверка типа введенного номера
        if not(isinstance(number, str)):
            raise IncorrectCarNumbers(f'Введён некорректный тип номера: {type(number)}', number)
    # Проверка длины номера (точно 6 символов)
        if len(number) != 6:
            raise IncorrectCarNumbers(f'Введён номер неверной длины: {len(number)} симв.', number)
        else:
            return True
# Функция создания объекта Car и заполения словаря созданных объектов
def cr_car(model, vin, number):
    # Определение максимального номера в словаре
    var_name_car = max([int(str(i)) for i in dict_car.keys()])
    key_car = f'{str(var_name_car + 1)}'
    # Проверка создания объекта Car
    try:
        dict_car[key_car] = car(model, vin, number)
    # Проверка наличия исключений
    except (IncorrectVinNumber, IncorrectCarNumbers) as err:
        print(f'Тип ошибки: {err.message}')
        print(f'Данные вызвавшие ошибку: {err.info}')
    # Создание в случае отсутствия ошибок
    else:
        dict_car[key_car] = car(model, vin, number)
        print('ОК')
# Вывод результатов с разными наборами данных
for i in range(0, 7):
    print(f'Создаем машину марки: {lst_name[i]}, VIN: {lst_VIN[i]}, Номер: {lst_num[i]}')
    cr_car(lst_name[i], lst_VIN[i], lst_num[i])
    print('-' * 20)
# Вывод словаря созданных объектов
print(f'Число созданных машин: {len([i for i in dict_car.keys()])-1}')










