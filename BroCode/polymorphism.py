# Polymorphism -> f concept in oop, allows objects of different classes to be treated as objects of a common superclass ( have many forms/faces )
# Two ways -> 
#   1. Inheritance - an object could be treated as of the same type as a parent class
#   2. Duck typing - object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return (self.base * self.height)/2
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(5), Square(6), Triangle(7, 8), Pizza("Sausages", 5)]

for shape in shapes:
    print(f"{shape.area()}cm²")
