# Создать человека. У него есть имя, возраст, пол, год рождения, работа, цель, домашнее животное 
# методы: идет на работу, кормит питомца 

import os
import time
from time import sleep 

os.system("clear")

class Elf:
    """
    Who is he?
    """

    def __init__(self, name, job, age, sex, year_of_birth, purpose, house_pet):
        self.name = name
        self.job = job
        self.age = age
        self.sex = sex
        self.year_of_birth = year_of_birth
        self.purpose = purpose
        self.house_pet = house_pet

    def get_name(self):
        return self.name + "Elf Legolas"

    def get_job(self):
        return self.name + "He's sharpshooter with an Elfian keen eye! This Elf kills Orks"

    def get_age(self):
        return self.name + "...2000 years old? 3000 years old? Right, several thousand years! But he still kills Orks" 

    def get_sex(self):
        return self.name + "an Elf...killing Orks"

    def get_year_of_birth(self):
        return self.name + "Unknown, but killing Orks during a thousand years!"

    def get_purpose(self):
        return self.name + "Hmmmm.... probably hunting Orks? Fighting with Aragorn and Gimmly?"

    def get_house_pet(self):
        return self.name + "he has no pet, but he has a BIG BEAUTIFUL BOW for killing these goddamn Orks!"

    def __str__(self):
        return f"Huh? Are we gonna hunt some Orks?"

elf1 = Elf("", "", "", "", "", "", "") 

print(elf1.get_name()) 
time.sleep(3)
print(elf1.get_job()) 
time.sleep(3)
print(elf1.get_age()) 
time.sleep(3)
print(elf1.get_sex()) 
time.sleep(3)
print(elf1.get_year_of_birth()) 
time.sleep(3)
print(elf1.get_purpose()) 
time.sleep(3)
print(elf1.get_house_pet()) 


