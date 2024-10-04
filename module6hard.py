from math import sqrt
class Figure:
    sides_count = 0  # количество сторон, изначально 0

    def __init__(self, filled, r, b, g, *sides):  # filled - закрашенный (True, False), цвета в формате RBG, стороны фигуры
        self.__sides = sides
        self.filled = bool(filled)
        self.__color = {"r": r, "b": b, "g": g}

    def get_color(self):  # возвращаем цвета
        return self.__color

    def __is_valid_color(self):  # проверка формата RBG задаваемых цветов
        if self.__color.get("r") <= 255 and self.__color.get("b") <= 255 and self.__color.get("g") <= 255 <= 255:
            return True
        else:
            return False

    def set_color(self, r, b, g):  # изменение цветов
        if self.__is_valid_color():
            self.__color = {"r": r, "b": b, "g": g}

    def __is_valid_sides(self, *side):  # проверка задаваемых сторон на их количество
        for item in self.__sides:
            if isinstance(item, int) and len(self.__sides) == len(side):
                return True
        else:
            return False

    def get_sides(self):  # возвращаем стороны фигуры
        return self.__sides

    def set_sides(self, *new_sides):  # изменение сторон
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides

    def __len__(self):  # переопределяем len в периметр
        return sum(self.__sides)


class Circle(Figure):  # класс круга
    sides_count = 1

    def __radius(self):  # находим радиус круга
        rad = len(self) / (2 * 3.14)
        return round(rad, 2)

    def get_square(self):  # находим площадь круга по радиусу
        s = 3.14 * self.__radius() ** 2
        return round(s, 2)


class Triangle(Figure):  # класс треугольника
    sides_count = 3      # кол-во сторон

    def get_square(self):   # находим площадь треугольника
        p = len(self) / 2
        s = sqrt(p*(p - self._Figure__sides[0])*(p - self._Figure__sides[1])*(p - self._Figure__sides[2])) # формула Герона
        return round(s, 2)


class Cube(Figure):  # класс куба
    sides_count = 12  # кол-во сторон куба

    def __init__(self, filled, r, b, g, sides):  # filled - закрашенный (True, False), цвета в формате RBG, стороны фигуры
        super().__init__(filled, r, b, g)
        sides_cube = []
        for i in range(12): sides_cube.append(sides)  # повторяем стороны 12 раз
        self._Figure__sides = sides_cube

    def get_volume(self):
        v = self._Figure__sides[0] ** 3   # находим объем по любой стороне
        return round(v, 2)






circle1 = Circle(True, 233, 245, 255, 15)
print("ПРОВЕРКА ФУНКЦИЙ КРУГА")
print(f'длина окружности - {len(circle1)}')
print(f'радиус круга - {circle1._Circle__radius()}')
print(f'площадь круга - {circle1.get_square()} \n')


triangle1 = Triangle(True, 233, 245, 255, 5, 7, 2)
print("ПРОВЕРКА ИЗМЕНЕНИЯ ЦВЕТА ( на треугольнике)")
print(f'цвета сейчас - {triangle1.get_color()}')
triangle1.set_color(12, 45, 255)
print(f'измененные цвета - {triangle1.get_color()} \n')

print("ПРОВЕРКА ИЗМЕНЕНИЯ СТОРОН (на треугольнике)")
print(f'список сторон треугольника - {triangle1.get_sides()}')
triangle1.set_sides(11, 9, 63, 56, 54, 4) # ничего не изменилось
triangle1.set_sides(3, 5, 6)
print(f'измененный список сторон треугольника - {triangle1.get_sides()}')
print(f'площадь треугольника - {triangle1.get_square()} \n')


cube1 = Cube(True, 112, 233, 245, 13)
print("ПРОВЕРКА ФУНКЦИЙ КУБА")
print(f'стороны куба - {cube1.get_sides()}')
print(f'объем куба - {cube1.get_volume()}')
