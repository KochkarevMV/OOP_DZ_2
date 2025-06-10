from abc import ABC, abstractmethod
import math


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


class Rectangle (FigureRectangle):
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


RectEx1 = Rectangle(2, 5)
RectEx2 = Rectangle(3, 8)
print(RectEx1.get_perimeter)
print(RectEx1.get_area)
print(RectEx2.get_area)
print(RectEx2.add_area(RectEx1))