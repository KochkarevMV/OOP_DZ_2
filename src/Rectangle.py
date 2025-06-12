from abc import ABC, abstractmethod


class FigureRectangle(ABC):
    
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, FigureRectangle):
            raise ValueError("Должна быть фигура. Уточните вводные")
        return self.get_area + other_figure.get_area


class Rectangle(FigureRectangle):
    def __init__(self, RectSideA, RectSideB):
        if RectSideA <= 0 or RectSideB <= 0:
            raise ValueError("Сторона прямоугольника должна быть больше нуля")
        self.RectSideA = RectSideA
        self.RectSideB = RectSideB

    @property
    def get_perimeter(self):
        return (self.RectSideA + self.RectSideB) * 2
    
    @property
    def get_area(self):
        return self.RectSideA * self.RectSideB
    

class SquareRect(Rectangle):
    def __init__(self, RectSideA):
        if RectSideA <= 0:
            raise ValueError("Сторона квадрата должна быть больше нуля")
        super().__init__(RectSideA, RectSideA)


RectEx1 = Rectangle(2, 5)
RectEx2 = Rectangle(3, 8)
Square1 = SquareRect(4)

print(f" Периметр RectEx1 равен {RectEx1.get_perimeter}")
print(f" Площадь RectEx1 равна {RectEx1.get_area}")
print(f" Площадь RectEx2 равна {RectEx2.get_area}")
print(f" Сумма площадей RectEx1 и RectEx2 равна {RectEx2.add_area(RectEx1)}")
print(f" Площадь Square1 равна {Square1.get_area}")
print(f" Сумма площадей RectEx1 и Squere1 равна {RectEx1.add_area(Square1)}")