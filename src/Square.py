from abc import ABC, abstractmethod
import math


class FigureSquare(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, FigureSquare):
            raise ValueError("Должна быть фигура. Проверьте данные")
        return self.get_area + other_figure.get_area
        

class Square(FigureSquare):
    def __init__(self, square_sideA):
        if square_sideA <= 0:
            raise ValueError("Сторона квадрата должна быть больше нуля")
        self.square_sideA = square_sideA

    @property
    def get_perimeter(self):
        return self.square_sideA*4
    
    @property
    def get_area(self):
        return self.square_sideA*self.square_sideA
    

SquareEx = Square(5)
SquareEx2 = Square(2)
print(SquareEx.get_perimeter)
print(SquareEx.get_area)
print(SquareEx2.get_area)
print(SquareEx2.add_area(SquareEx))