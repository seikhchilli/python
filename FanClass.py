class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self, speed = SLOW, on = False, radius = 5, color = "Blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    
    def getSpeed(self):
        return self.__speed
    
    def setSpeed(self, spd):
        self.__speed = spd
    
    def getOn(self):
        return self.__on
    
    def setOn(self, ons):
        self.__on = ons
    
    def getRadius(self):
        return self.__radius 
    
    def setRadius(self, rad):
        self.__radius = rad
    
    def getColor(self):
        return self.__color
    
    def setColor(self, clr):
        self.__color = clr
    

def main():
    fan1 = Fan(speed = Fan.FAST, on = True, radius = 10, color = "Yellow")
    fan2 = Fan(speed = Fan.MEDIUM, on = False, radius = 5, color = "Blue")

    print("Speed of Fan1: ", fan1.getSpeed())
    print("Speed of Fan2: ", fan2.getSpeed())
    print("Radius of Fan1: ", fan1.getRadius())
    print("Radius of Fan2: ", fan2.getRadius())
    print("Color of Fan1: ", fan1.getColor())
    print("Color of Fan2: ", fan2.getColor())
main()
