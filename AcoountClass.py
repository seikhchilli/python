class Account:
    def __init__(self):
        self.__id = 0
        self.__balance = 100
        self.__annualInterestRate = 0
    
    def getId(self):
        return self.__id
    
    def setId(self, Id):
        self.__id = Id
    
    def getBalance(self):
        return self.__balance
    
    def setBalance(self, bal):
        self.__balance = bal
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setAnnualInterestRate(self, rate):
        self.__annualInterestRate = rate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12
    
    def getMonthlyInterest(self):
        return (self.__balance * self.__annualInterestRate / 12 )/100
    
    def withdraw(self, withbal):
        self.__balance = self.__balance - withbal
    
    def deposit(self, depobal):
        self.__balance += depobal
    

def main():
    a = Account()
    a.setId(1122)
    a.setBalance(20000)
    a.setAnnualInterestRate(4.5)
    a.withdraw(2500)
    a.deposit(3000)

    print("Id: ", a.getId())
    print("Balance: ", a.getBalance())
    print("Monthly Interest rate: ", a.getMonthlyInterestRate())
    print("Monthly Interest: ", a.getMonthlyInterest())

main()
