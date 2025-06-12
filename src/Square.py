from abc import ABC, abstractmethod


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
    

class Rectangle(Square):
    def __init__(self, square_sideA, square_sideB):
        self.square_sideB = square_sideB
        if square_sideA <= 0 or square_sideB <= 0:
            raise ValueError("Сторона прямоугольника должна быть больше нуля")
        super().__init__(square_sideA)


SquareEx = Square(5)
SquareEx2 = Square(2)
Rectangle1 = Rectangle(3, 5)
print(f" Периметр SquareEx равен {SquareEx.get_perimeter}")
print(f" Площадь SquareEx равна {SquareEx.get_area}")
print(f" Площадь SquareEx2 равна {SquareEx2.get_area}")
print(f" Сумма площадей SquareEx и SquareEx2 равна {SquareEx2.add_area(SquareEx)}")
print(f" Площадь Rectangle1 равна {Rectangle1.get_area}")
print(f" Сумма площадей SquareEx и Rectangle1 равна {SquareEx.add_area(Rectangle1)}")