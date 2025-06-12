from abc import ABC, abstractmethod
import math


class FigureTri(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass
     
    def add_area(self, other_figure):
        if not isinstance(other_figure, FigureTri):
            raise ValueError("Аргументом должна быть фигура. Проверьте данные")
        return self.get_area + other_figure.get_area
   

class Triangle (FigureTri):
    def __init__(self, triA, triB, triC):
        if triA == triB or triA == triC or triB == triC:
            raise ValueError("Стороны треугольника должны быть разными по длине")
        if triA+triB == triC or triA+triC == triB or triC+triB == triA:
            raise ValueError("Сумма двух сторон не должна быть равна длине третьей")
        if triA <= 0 or triB <= 0 or triC <= 0:
            raise ValueError("Длина сторон должна быть больше нуля")
        self.triA = triA
        self.triB = triB
        self.triC = triC
        
    @property
    def get_perimeter(self):
        return self.triA + self.triB + self.triC

    @property
    def get_area(self):
        triP = (self.triA + self.triB + self.triC)/2
        triS = math.trunc(math.sqrt(triP*(triP-self.triA)*(triP-self.triB)*(triP-self.triC)))
        return triS


Tri1 = Triangle(4, 3, 5)
Tri2 = Triangle(4, 3, 2)

print(Tri1.get_area)
print(Tri2.get_area)
print(Tri1.get_perimeter)
print(Tri1.add_area(Tri2))
print(Tri2.add_area(Tri1))