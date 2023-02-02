class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
 
    def add(self):
        return self.num1 + self.num2
 
    def subtract(self):
        return self.num1 - self.num2
 
    def multiply(self):
        return self.num1 * self.num2
 
    def divide(self):
        return self.num1 / self.num2 

n1 = int(input("Введите два числа: ")) 
n2 = int(input()) 

calc = Calculator(n1, n2) 

print("Сумма равна: ", calc.add()) 
print("Разность равна: ", calc.subtract()) 
print("Произведение равно: ", calc.multiply()) 
print("Частное равно: ", calc.divide()) 



