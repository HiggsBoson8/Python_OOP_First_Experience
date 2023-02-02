# a = "123123qwe" # строка

# print(a.capitalize()) # метод строки
# print(type(a)) # class string - класс стринг имеет свои методы внутри

import os 
import time 
from time import sleep

os.system("clear") 

# название класса должно быть с большой буквы
class Cat:
    """
    Для чего этот класс!
    """

    # def init - initialize method
    def __init__(self, name, age): # классы не сильно отличаются от функции, все атрибуты нужно передать в init
        # self - маршрутизатор, ссылается
        self.name = name 
        self.age = age 


    # создаем методы класса
    def meow(self): 
        return self.name + " is meowing!"

    def eat(self):
        return self.name + " кушает"

    def play(self):
        return self.name + " играет" 

    def sleep(self):
        return self.name + " уснул"

    def __str__(self):
        return f"Вы не указали что вернуть"

cat1 = Cat("Муси", 2) # экземпляр класса
cat2 = Cat("Герман", 3) # экземпляр класса

# print(cat1.name, cat1.age, cat1.meow()) 
# print(cat1.meow())

print(cat2.meow())
time.sleep(3)

print(cat2.eat())
time.sleep(3)

print(cat2.play())
time.sleep(3)

print(cat2.sleep())

