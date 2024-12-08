class Figure:
    sides_count = 0

    def __init__(self, color, sides: int, filled=False):
        self.__sides = sides
        self.__color = list(color)
        self.filled = filled


    def get_color(self):
        return self.__color
        # возвращает список RGB цветов


    def __is_valid_color(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return r, g, b
        # Метод __is_valid_color - служебный, принимает параметры r, g, b,
        # который проверяет корректность переданных значений перед установкой
        # нового цвета. Корректным цвет: все значения r, g и b - целые числа
        # в диапазоне от 0 до 255 (включительно).


    def set_color(self, r: int, g: int, b: int):
        new_color = self.__color
        if new_color == self.__is_valid_color(r, g, b):
            return new_color
        else:
            return self.__color
        # принимает параметры r, g, b - числа и изменяет атрибут __color
        # на соответствующие значения, предварительно проверив их на корректность.
        # Если введены некорректные данные, то цвет остаётся прежним.


    def __is_valid_sides(self, *new_sides_count):
        if len(new_sides_count) == self.sides_count and all(isinstance(side, int)
        and side > 0 for side in new_sides_count):
            return True
        else:
            return False
        # служебный, принимает неограниченное кол-во сторон, возвращает True если
        # все стороны целые положительные числа и кол-во новых сторон совпадает с
        # текущим, False - во всех остальных случаях.

    def get_sides(self):
        return self.__sides
        # должен возвращать значения атрибута __sides.

    def __len__(self):
        return sum(self.__sides)
        # должен возвращать периметр фигуры.


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            return self.__sides
        # должен принимать новые стороны, если количество сторон не равно sides_count,
        # то не изменять, в противном случае - менять.


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (2 * 3.14)
        # Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).


    def get_square(self):
        return  3.14 * (self.__radius ** 2)
        # возвращает площадь круга (можно рассчитать как через длину, так и через радиус).



class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = self.__len__() / 2
        return ((p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))) ** 0.5
        # возвращает площадь треугольника.(можно рассчитать по формуле Герона).


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, new_sides_cube):
        sides = [new_sides_cube] * self.sides_count
        super().__init__(color, sides)
        # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона).



    def get_volume(self):
        new_sides_cube = self.get_sides()[0]
        return new_sides_cube ** 3
        # возвращает объём куба.


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 200, 100), 10)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(circle1.get_square())
triangle1.set_sides(3, 4, 5)
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print(triangle1.get_square())