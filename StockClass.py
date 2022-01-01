class Stock:
    def __init__(self):
        self.__symbol = "INTC"
        self.__name = "Intel Corporation"
        self.__previousClosingPrice = 20.5
        self.__currentPrice = 20.35
    
    def getSymbol(self):
        return self.__symbol
    
    def getName(self):
        return self.__name
    
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    
    def getCurrentPrice(self):
        return self.__currentPrice
    
    def setPreviousClosingPrice(self, pcp):
        self.__previousClosingPrice = pcp
    
    def setCurrentPrice(self, cp):
        self.__currentPrice = cp
    
    def getChangePercent(self):
        return (((self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice) * 100)
    

def main():
    s = Stock()
    print("Previous closing price of stock: ", s.getPreviousClosingPrice())
    print("Current Price of stock: ", s.getCurrentPrice())
    print("Change percent in stokc price: ", s.getChangePercent())


main()
