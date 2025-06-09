from abc import ABC, abstractmethod
import math


class Figure(ABC):
    
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass
     
    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Аргументом должна быть фигура. Проверьте данные")
        return self.get_area + other_figure.get_area
   

class Triangle (Figure):
    def __init__(self, triA, triB, triC):
        if triA == triB or triA == triC or triB == triC:
            raise ValueError("Стороны треугольника должны быть разными")
        self.triA = triA
        self.triB = triB
        self.triC = triC


@property
def get_perimeter(self):
    return self.triA + self.triB + self.triC


@property
def get_area(self):
    triP = (self.triA + self.triB + self.triC)/2
    triS = math.sqrt(triP*(triP-self.triA)*(triP-self.triB)*(triP-self.triC))
    return triS


TriExx = Triangle(6, 8, 10)
print(TriExx.get_area)