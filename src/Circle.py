from abc import ABC, abstractmethod
import math


class FigureCirc(ABC):
    
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, FigureCirc):
            raise ValueError("Аргументом должна быть фигура. Проверьте данные")
        return self.get_area + other_figure.get_area
    

class Circle(FigureCirc):
    def __init__(self, circleRadius):
        if circleRadius <= 0:
            raise ValueError("Радиус круга должен быть больше нуля")
        self.circleRadius = circleRadius

    @property
    def get_perimeter(self):
        circlePerimetr = math.trunc(2*math.pi*self.circleRadius)
        return circlePerimetr
    
    @property
    def get_area(self):
        circleArea = math.trunc(math.pi*(self.circleRadius**2))
        return circleArea
    

class Triangle (Circle):
    def __init__(self, TriA, TriB, TriC, circleRadius):
        self.TriA = TriA
        self.TriB = TriB
        self.TriC = TriC
        super().__init__(circleRadius)
    
    @property
    def get_area(self):
        TriArea = math.trunc((self.TriA * self.TriB * self.TriC) / (4 * self.circleRadius))
        return TriArea


Circle1 = Circle(7)
Circle2 = Circle(5)
Triangle1 = Triangle(4, 3, 5, 8)


print(f" Периметр Circle1 равен {Circle1.get_perimeter}")
print(f" Площадь Circle1 равна {Circle1.get_area}")
print(f" Площадь Circle2 равна {Circle2.get_area}")
print(f" Сумма площадей Circle1 и Circle2 равна {Circle1.add_area(Circle2)}")
print(f" Площадь Triangle1 равна {Triangle1.get_area}")
print(f" Сумма площадей Circle1 и Triangle 1 равна {Triangle1.add_area(Circle1)}")