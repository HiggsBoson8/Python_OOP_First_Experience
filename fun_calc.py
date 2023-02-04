class Calculator():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return f"{self.num1 + self.num2} -> * сложить"

    def substract(self):
        return f"{self.num1 - self.num2} -> - вычесть"

    def multiply(self):
        return f"{self.num1 * self.num2} -> * умножить" 

    def divide(self):
        try:
            return f"{self.num1 / self.num2} -> / деление"
        except ZeroDivisionError:
            return "На ноль делить нельзя"

    def exponentiation(self):
        return f"{self.num1 ** self.num2} -> ** возведение в степень"

    def integer_division(self): 
        return f"{self.num1 // self.num2} -> // целочисленное деление"

    def remainder_of_division(self):
        return f"{self.num1 % self.num2} -> % остаток от деления"

    def __str__(self):
        return "error"

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

calc = Calculator(num1, num2)

print(calc.add())
print(calc.substract())
print(calc.multiply())
print(calc.divide())
print(calc.exponentiation())
print(calc.integer_division())
print(calc.remainder_of_division())


# ----------------------------------------------------------------


#----------------------------------------------------------------

# import pprint
# import os
# os.system("clear")


# class Calculator():

#     def __init__(self, symbol, num1, num2, operator):
#         self.symbol = symbol
#         self.num1 = num1
#         self.num2 = num2
#         self.operator = {}

#     def update(self):
#         self.operator.update({
#             f"{self.symbol}": {
#                "add": self.num1 + self.num2,
#                 "substract": self.num1 - self.num2,
#                 "multiply": self.num1 * self.num2,
#                 "divide": self.num1 / self.num2
#             }})
#         return self.operator

#     def __str__(self):
#         return self.symbol

# calc = Calculator("", "", "", "")

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# pprint.pprint(calc.update())
# print(calc.add())

