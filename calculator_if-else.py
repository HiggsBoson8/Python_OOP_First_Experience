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
        return self.num1 + self.num2 

    def minus(self):
        return self.num1 - self.num2 

    def divide(self):
        return self.num1 / self.num2

    def multiply(self):        
        return self.num1 * self.num2
    
    def __str__(self):
        return f"error"


operator = input("Enter and operator: (+ - / * % **): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

calc = Calculator(num1, num2)

if operator == "+":
    print(f"Addition: {calc.plus()}")
elif operator == "-":
    print(f"Subtraction: {calc.plus()}")
elif operator == "/":
    print(f"Division: {calc.divide()}")
elif operator == "*":
    print(f"Multiplication: {calc.multiply()}")
else:
    print("Invalid operator")


