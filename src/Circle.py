from abc import ABC, abstractmethod
import math


class Figure (ABC):
    
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
    

class Circle(Figure):
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
    

Circle1 = Circle(7)
Circle2 = Circle(5)

print(Circle1.get_perimeter)
print(Circle1.get_area)
print(Circle2.get_area)
print(Circle1.add_area(Circle2))