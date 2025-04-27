# @property -> decorator used to define a method (it can be accessed like an attribute)
# Benefit -> add additional logic regarding read, write or delete attributes (getter, setter, deleter method)

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f}cm"

    @property
    def height(self):
        return f"{self._height:.2f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

r = Rectangle(5.123, 6.456)
print(r.width)
print(r.height)