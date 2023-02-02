# Собрать железо?

import os 
import time 
# from time import sleep
# os.system("sleep")


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
        return self.video_card + "Мощная видюха для задрота" 
    
    def CPU(self):
        return  self.video_card + "Мощный процессор для игромана"

    def SSD(self):
        return f"По больше памяти для игр, потому что задрот будет качать много игр {self.ssd_harddisk}"
    
    def RAM(self):
        return f"И конечно же побольше оперативной памяти, потому что игры требуют много памяти"

    def __str__(self):
        return f"hmmmmmmmm"

zadrot = Computer("", "", "", "")

print(zadrot.video()) 
time.sleep(4)
print(zadrot.CPU())
time.sleep(4)
print(zadrot.RAM())
time.sleep(4)
print(zadrot.SSD())






