import math


class Figure:
    sides_count = 0

    def __init__(self, color: list[int], *sides, filled=True):
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            raise ValueError("Entered colors is not valid")

        self.__sides = sides  # self.set_sides(*sides)

        self.filled = filled

    @property
    def sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, r, g, b):
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        valid_values = 0 <= r <= 250 and 0 <= g <= 250 and 0 <= b <= 250

        if valid_types and valid_values:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            pass

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def __len__(self):
        """Return perimeter"""
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            # self.__sides = [1] * self.sides_count
            return None

        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            # return sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, length, filled=True):
        super().__init__(color, length, filled=filled)
        self.__radius = length / 2 * math.pi

    def get_square(self):
        return self.__radius ** 2 * math.pi


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=True):
        super().__init__(color, *sides, filled=filled)

    def get_square(self):
        p_triangle = len(self) // 2
        print(self.sides[0], self.sides[1], self.sides[2])
        p_square = math.sqrt(p_triangle * (p_triangle - self.sides[0]) *
                             (p_triangle - self.sides[1]) *
                             (p_triangle - self.sides[2]))
        return p_square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side, filled=False):
        sides = [side] * self.sides_count
        super().__init__(color, *sides, filled=filled)

    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())




