# super() -> function used in a child class to call methods from a parent class(superclass)
#allows you to extend the functionality of the inherited methods

import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, radius, color, is_filled):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"This triangle has an area of {math.pi*self.radius*self.radius} m^2")

class Square(Shape):
    def __init__(self, side, color, is_filled):
        super().__init__(color, is_filled)
        self.side = side

    def describe(self):
        super().describe()
        print(f"This square has an area of {self.side*self.side} m^2")

class Triangle(Shape):
    def __init__(self, base, color, is_filled, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    def describe(self):
        super().describe()
        print(f"This triangle has an area of {0.5*self.base*self.height} m^2")

c = Circle(5, "Blue", False)
s = Square(5, "Red", True)
t = Triangle(10, "Purple", True, 15)

print(t.describe())
print(c.describe())
print(s.describe())