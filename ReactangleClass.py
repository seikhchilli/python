class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def getArea(self):
        area = self.width * self.length
        return area
        
    def getPerimeter(self):
        perimeter = 2 * (self.width + self.length)
        return perimeter

def main():
    r = Rectangle(2, 3)
    print("Area: ", r.getArea())
    print("Perimeter: ", r.getPerimeter())

main()

    
    