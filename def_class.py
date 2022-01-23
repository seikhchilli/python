import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
    def getArea(self):
        return math.pi * self.radius ** 2
    
    def setRadius(self, radius):
        self.radius = radius

def main():
    c1 = Circle(5)
    c2 = Circle(7)

    print("Radius of C1: ", c1.radius)
    print("Radius of C2: ", c2.radius)

    print("\nPerimeter of C1: ", c1.getPerimeter())
    print("Perimeter of C2: ", c2.getPerimeter())

    print("\nArea of C1: ", c1.getArea())
    print("Area of C2: ", c2.getArea())
    


main()