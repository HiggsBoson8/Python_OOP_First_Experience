# Собрать железо?

import os 
import time 
import os
os.system('clear')


class Computer:
    """
    Собираем игровое железо для задрота
    """

    def __init__(self, video_card, central_processing_unit, ssd_harddisk, random_access_memory):
        self.video_card = video_card
        self.central_processing_unit = central_processing_unit
        self.ssd_harddisk = ssd_harddisk
        self.random_access_memory = random_access_memory
        
    def video(self):
        return f"Мощная видюха {self.video_card} для задрота" 
    
    def CPU(self):
        return f"Мощный процессор для игромана + {self.central_processing_unit}"

    def SSD(self):
        return f"По больше памяти для игр, потому что мальчишка будет качать много игр, поэтому и {self.ssd_harddisk}"
    
    def RAM(self):
        return f"И конечно же побольше оперативной памяти, потому что игры требуют много памяти + {self.random_access_memory} для задрота! Ведь мальчишка будет играть сразу в несколько игр одновременно!"

    def __str__(self):
        return f"hmmmmmmmm"

zadrot = Computer("NVIDIA Geforce RTX 5080ti super nerd", "AMD RYZEN 10 9800x super nerd edition", "SSD 10tb", "64gb RAM")

print("И так, давайте соберем мощный игровой компуктор для малолетнего задрота! Что мы ему дадим? ")
time.sleep(4)
print(zadrot.video()) 
time.sleep(4)
print(zadrot.CPU())
time.sleep(4)
print(zadrot.RAM())
time.sleep(4)
print(zadrot.SSD())
time.sleep(6)
print("?????????????????? \nPROFIT \nМальчишка счастлив!")

