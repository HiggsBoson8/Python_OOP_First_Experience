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
    def __init__(self, name, age, breed): # классы не сильно отличаются от функции, все атрибуты нужно передать в init
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

    
cat1 = Cat("Муси", 2, "оранжевая кошка") # экземпляр класса
cat2 = Cat("Никс", 11, "белый котик") # экземпляр класса
cat3 = Cat("Кеша", 5, "черный котик")
cat4 = Cat("Шушуина", 3, "коричневая кошка")
cat5 = Cat("Монк", 10, "мейн-кун")


# print(cat1.name, cat1.age, cat1.meow()) 
# print(cat1.meow())

# print(cat1.meow())
# time.sleep(3)
# print(cat1.eat())
# time.sleep(3)
# print(cat1.play())
# time.sleep(3)
# print(cat1.sleep())


print(cat1.eat())
time.sleep(3)
print(cat2.eat()) 
time.sleep(3)
print(cat3.eat()) 
time.sleep(3)
print(cat4.eat()) 
time.sleep(3)
print(cat5.eat()) 
time.sleep(3)

print("Все котики сытые и довольные!")






