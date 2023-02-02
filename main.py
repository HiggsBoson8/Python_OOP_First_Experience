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
        return f"Elf {self.name}"

    def get_job(self):
        return f"{self.name}'s {self.job}! This Elf kills Orks"

    def get_age(self):
        return f"{self.age} But he still kills Orks" 

    def get_sex(self):
        return f"{self.name} is a {self.sex} and he kills huge number of the Orks!" 

    def get_year_of_birth(self):
        return f"When is his year of birth? {self.year_of_birth}, but {self.name}'s killing Orks during a thousand years!"

    def get_purpose(self):
        return f"{self.purpose} Yeah, right! Purpose is killing Orks."

    def get_house_pet(self):
        return f"{self.name} {self.house_pet} but he has a BIG BEAUTIFUL BOW for killing goddamn Orks!"

    def __str__(self):
        return f"Huh? Are we gonna hunt some Orks?"

    
elf1 = Elf("Legolas", "sharpshooter with an Elfian keen eye", "...2000 years old? 3000 years old? Right, several thousand years!",\
"male Elf", "Unknown", "Hmmmm, no idea...probably hunting Orks? Fighting with Aragorn and Gimmly?",\
"has no pet") 


print(elf1.get_name()) 
time.sleep(3)
print(elf1.get_job()) 
time.sleep(4)
print(elf1.get_age()) 
time.sleep(4)
print(elf1.get_sex()) 
time.sleep(4)
print(elf1.get_year_of_birth()) 
time.sleep(4)
print(elf1.get_purpose()) 
time.sleep(4)
print(elf1.get_house_pet()) 
time.sleep(4)
print("Huh? Are we gonna hunt some Orks?")



