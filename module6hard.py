import math

class Figure():
    sides_count = 0
    def __init__(self, sides, red, green, blue, filled = False):
        self.__sides = []
        if self.sides_count == 0:
            self.__sides = []
        elif len(sides) != self.sides_count:
            for i in range(0, self.sides_count):
                self.__sides.append(1)
        elif len(sides) == self.sides_count:
            for i in range(0, self.sides_count):
                self.__sides.append(sides[i])
        self.__color = self._Figure__is_valid_color(red, green, blue)[1]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, red, green, blue):
        valid = [False, False, False]
        rgb = [red, green, blue]
        for i in range (0,3):
            valid[i] = rgb[i] in range(0,255) and type(rgb[i]) == int
        if False in valid:
            return self, None
        else:
            return self, rgb

    def set_color(self, red, green, blue):
        check = self._Figure__is_valid_color(red, green, blue)[1]
        if check:
            self.__color = self._Figure__is_valid_color(red, green, blue)[1]

    def  __is_valid_sides(self, lst_sides):
        res = self.sides_count == len(lst_sides)
        for i in lst_sides:
            res = res and (i in range(0,255) and type(i) == int)
        return res

    def get_sides(self):
        return self._Figure__sides

    def set_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            self._Figure__sides.clear()
            self._Figure__sides = new_sides
        else:
            return None

    def __len(self):
        if self.sides_count == 0:
            return None
        elif self.sides_count == 1:
            return round(self.__sides[0]*math.pi, 3)
        elif self.sides_count == 3 or self.sides_count == 12:
            perim = 0
            for i in self._Figure__sides:
                perim = perim + i
            return perim


class Circle(Figure):
    sides_count = 1
    def __radius(self):
        return self._Figure__sides[0]

    def get_square(self):
        return round(math.pow(self._Figure__sides[0],2)*math.pi,3)

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        p = self._Figure__len()/2
        s = round(math.pow(p*(p-self.get_sides()[0])*(p-self.get_sides()[1])*(p-self.get_sides()[2]),0.5),3)
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, sides, red, green, blue, filled = False):
        self._Figure__sides = []
        if len(sides) == 1:
            for i in range(0, 12):
                self._Figure__sides.append(sides[0])
        elif len(sides) != 12:
            for i in range(0, 12):
                self._Figure__sides.append(1)
        else:
            for i in range(0, 12):
                self._Figure__sides.append(sides[i])
        self._Figure__color = self._Figure__is_valid_color(red, green, blue)[1]
        self.filled = filled

    def set_sides(self, new_sides):
        self._Figure__sides.clear()
        if len(new_sides) == 1:
            for i in range(0, 12):
                self._Figure__sides.append(new_sides[0])
        elif len(new_sides) != 12:
            for i in range(0, 12):
                self._Figure__sides.append(1)
        else:
            for i in range(0, 12):
                self._Figure__sides.append(new_sides[i])

    def get_volume(self):
        return math.pow(self._Figure__sides[0],3)

# # Тестовые данные
# lst_color_00 = [151, 152, 153]
# lst_color = [101, 102, 103]
# lst_sides = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10] # 15 чисел
# lst_sides_00 = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11] # 15 чисел
#
# f00 = Figure(lst_sides, *lst_color_00)
# c00 = Circle(lst_sides, *lst_color_00)
# t00 = Triangle(lst_sides, *lst_color_00)
# cb00 = Cube(lst_sides, *lst_color_00)
#
# # Блок тестирования методов
# print('00',f00.get_sides(), c00.get_sides(), t00.get_sides()) # Получение длин сторон из Figure, Circle и Triangle
# print('01', cb00.get_sides()) # Получение длин сторон из Cube
# print('02',f00.get_color()) # Получение RGB из Figure
# check_color = f00._Figure__is_valid_color(*lst_color) # Проверка переданных значений RGB на валидность
# if check_color[1]:
#     f00.set_color(*check_color[1]) # Установка переданных значений RGB в Figure
# else:
#     print(f'В переданных данных для {next(key for key, value in globals().items() if value == check_color[0])} ошибка')
# print('03',f00.get_color()) # Получение RGB из Figure
# print('04',f00._Figure__is_valid_sides(lst_sides)) # Проверка переданного списка сторон на тип и значение
# print('05',f00.get_color(), c00.get_color()) # Получение RGB из Figure и Circle
# check_color = c00._Figure__is_valid_color(*lst_color) # Проверка переданных значений RGB на валидность
# if check_color[1]:
#     c00.set_color(*check_color[1]) # Установка переданных значений RGB в Circle
# else:
#     print(f'В переданных данных для {next(key for key, value in globals().items() if value == check_color[0])} ошибка')
# print('06',f00.get_color(), c00.get_color()) # Получение RGB из Figure и Circle
# print('07',f00.get_sides(), c00.get_sides()) # Получение длин сторон из Figure и Circle
# f00.set_sides(lst_sides[:1]) # Установка значений сторон Figure
# c00.set_sides(lst_sides[:1]) # Установка значений сторон Circle
# t00.set_sides(lst_sides[:3]) # Установка значений сторон Triangle
# cb00.set_sides(lst_sides[:12]) # Установка значений сторон Cube списком сторон
# print('08',f00.get_sides(), c00.get_sides(), t00.get_sides()) # Получение длин сторон из Figure, Circle и Triangle
# print('09', cb00.get_sides()) # Получение длин сторон из Cube
# cb00.set_sides(lst_sides_00) # Установка значений сторон Cube списком сторон при передаче числа значений больше 12
# print('10', cb00.get_sides()) # Получение длин сторон из Cube
# print('11',f00._Figure__len(), c00._Figure__len()) # Расчет периметра для Figure и Circle
# print('12',t00._Figure__len(), cb00._Figure__len()) # Расчет периметра для Triangle и Cube
# print('13',c00._Circle__radius()) # Получение радиуса для Circle
# print('14',c00.get_square()) # Расчет площади Circle
# print('15',t00.get_square()) # Расчет площади Triangle
# print('16',cb00.get_volume()) # Расчет объема Cube
# cb00.set_sides(lst_sides[:12]) # Установка значений сторон Cube, по первому значения списка сторон
# print('17', cb00.get_sides()) # Получение длин сторон из Cube
# print('18', cb00._Figure__len()) # Расчет периметра для Cube
# print('19',cb00.get_volume()) # Расчет объема Cube
print('-'*20)
# Отработка примеров
    # Исходные данные
        # Цвета
rgb_tst_00 = [200, 200, 100]
rgb_tst_01 = [222, 35, 130]
rgb_tst_02 = [300, 70, 15]
        # Наборы сторон
lst_sides_tst00 = [10, 15, 6]
lst_sides_tst01 = [10, 6]
lst_sides_tst02 = [9]
lst_sides_tst03 = [9, 12]
lst_sides_tst04 = [10]
lst_sides_tst05 = [5, 3, 12, 4, 5]
lst_sides_tst06 = [15]
lst_sides_tst07 = [6]
    # Создание объектов
c01 = Circle(lst_sides_tst00, *rgb_tst_00) # Создание объекта c01 (000)
c02 = Circle(lst_sides_tst04, *rgb_tst_00) # Создание объекта c02 (001)
t01 = Triangle(lst_sides_tst01, *rgb_tst_00) # Создание объекта t01 (002)
cb01 = Cube(lst_sides_tst02, *rgb_tst_00) # Создание объекта cb01 (003)
cb02 = Cube(lst_sides_tst03, *rgb_tst_00) # Создание объекта cb02 (004)
    # Вывод параметров созданных объектов
print('000', c01.get_color(), c01.get_sides())
print('001', c02.get_color(), c02.get_sides())
print('002', t01.get_color(), t01.get_sides())
print('003', cb01.get_color(), cb01.get_sides())
print('004', cb02.get_color(), cb02.get_sides())
    # Проверка на изменение цветов:
c01.set_color(55, 66, 77) # Изменение цветов объекта c01 (005)
cb01.set_color(*rgb_tst_02) # Изменение цветов объекта cb01 (006)
    # Вывод результатов изменений
print('005', c01.get_color())
print('006', cb01.get_color())
    # Проверка на изменение сторон:
cb01.set_sides(lst_sides_tst05) # Изменение сторон объекта cb01
c01.set_sides(lst_sides_tst06)  # Изменение сторон объекта c01
    # Вывод результатов изменений
print('008', cb01.get_sides())
print('009', c01.get_sides())
    # Проверка периметра (круга) c01, это и есть длина:
print('010',c01._Figure__len())
    # Проверка объёма (куба) cb01:
cb01.set_sides(lst_sides_tst07) # Изменение сторон объекта cb01
print('011', cb01.get_volume())





