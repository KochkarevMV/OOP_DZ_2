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
   

class Triangle(FigureTri):
    def __init__(self, triA, triB, triC):
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


class Circle(Triangle):
    def __init__(self, triA, circleRadius):
        self.triA = triA
        triP = (self.triA + self.triA + self.triA)/2
        triS = math.trunc(math.sqrt(triP*(triP-self.triA)*(triP-self.triA)*(triP-self.triA)))
        self.circleRadius = circleRadius
        circleRadius = triS / triP
        super().__init__(triA, triA, triA)
    
    @property
    def get_area(self):
        CircleArea = math.trunc((self.triA * self.triA * self.triA) / (4 * self.circleRadius))
        return CircleArea


Tri1 = Triangle(4, 3, 5)
Tri2 = Triangle(4, 3, 2)
Circle1 = Circle(4, 8)


print(f" Площадь Tri1 равна {Tri1.get_area}")
print(f" Площадь Tri2 равна {Tri2.get_area}")
print(f" Периметр Tri1 равен {Tri1.get_perimeter}")
print(f" Сумма площадей Tri1 и Tri2 равна {Tri1.add_area(Tri2)}")
print(f" Площадь Circle1 равна {Circle1.get_area}")
print(f" Сумма площадей Circle1 и Tri1 равна {Circle1.add_area(Tri1)}")