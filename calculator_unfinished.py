import os
import time
from time import sleep 

os.system("clear")



class Calculator:
    """
    We gonna calculate 
    """



    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):    
        if operator == "+":
            return self.num1 + self.num2 

    def minus(self):
        if operator == "-":
            return self.num1 - self.num2 

    def divide(self):        
        if operator == "/":
            return self.num1 / self.num2

    def multiply(self):        
        if operator == "*":
            return self.num1 * self.num2
    
    def __str__(self):
        return f"error"


operator = input("Enter and operator: (+ - / * % **): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

calc = Calculator(num1, num2, operator)


print(calc.plus())
print(calc.minus())
print(calc.divide())
print(calc.multiply())


