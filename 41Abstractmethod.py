from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def printarea(self):
        return self.length * self.breadth
class Square(Rectangle):
    def __init__(self):
        self.length = 5
        self.breadth  = 5
rect = Rectangle()
sq = Square()
print(rect.printarea(),sq.printarea())
# polygon = Shape() 