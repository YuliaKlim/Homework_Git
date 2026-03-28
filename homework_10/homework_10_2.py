from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return self.__class__.__name__

class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return self.__side_length ** 4

class Rectangle(Figure):
    def __init__(self, side_length, side_width):
        self.__side_length = side_length
        self.__side_width = side_width

    def area(self):
        return self.__side_length * self.__side_width

    def perimeter(self):
        return self.__side_length * 2 + self.__side_width * 2

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return int(3.14 * self.__radius ** 2)

    def perimeter(self):
        return int(2 * 3.14 * self.__radius)

for figure in [Square(8), Rectangle(8, 3), Circle(5)]:
    print(f'Area of a {figure}:', figure.area())
    print(f'Perimeter of a {figure}:', figure.perimeter())