class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides):
        self.__sides = __sides
        self.__color = __color
        self.filed = False
        self.__perimetr = 0

    def get_color(self):
        return self.__color

    def _is_valid_color(self, r: int, g: int, b: int):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def _is_valid_sides(self, args):
        if len(args) == self.sides_count and all(
                isinstance(side, int) for side in args):
            return True

    def set_color(self, r: int, g: int, b: int):
        if self._is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *args):
        if self._is_valid_sides(args):
            self.__sides = args

    def __len__(self):
        self.__perimetr = 0
        for i in self.__sides:
            self.__perimetr += i
        return self.__perimetr


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / 2 * 3.14

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3
    p = 0

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.get_sqare(sides) * 2 / sides[0]

    def get_sqare(self, sides):
        Triangle.p = (sides[0] + sides[1] + sides[2]) / 2
        return (2 * (Triangle.p * (Triangle.p - sides[0]) *
                     (Triangle.p - sides[1]) * (Triangle.p - sides[2]))**0.5)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides * self.sides_count

    def get_volume(self):
        return self.__sides[0] * self.__sides[1] * self.__sides[2]


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
