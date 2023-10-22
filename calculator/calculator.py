class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def checkdata(self):
        pass

    def add(self):
        return self.num1+self.num2
    
    def subtract(self):
        return self.num1-self.num2
    
    def multiply(self):
        return self.num1*self.num2
    
    def divide(self):
        try:
            return self.num1/self.num2
        except ZeroDivisionError:
            return "You cannot devide by 0"
        