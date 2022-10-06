import random,time
import tkinter as tk
import customtkinter as ct
import pygame
from pygame.locals import *
from pygame import mixer

#==============Music Player ===============
def PlayBGMusic():
    mixer.init()
    mixer.music.load(r'SRC\Assets\SFX\bgmusic.mp3')
    mixer.music.play()
#============== Difficulty  ===============
# 0 = easy
# 1 = medium
# 2 = hard
# 3 = nightmare

def GiveQuestion():
    global GameDifficulty
    
    if GameDifficulty == 0:
        print("Easy Question")
        return 0

    elif GameDifficulty == 1:
        print("Medium Question")
        return 1

    elif GameDifficulty == 2:
        print("Hard Question")
        return 2

    else:
        print("Nightmare Question")
        return 3
#===========================================

     
   
def SavePlayeroints():
    print("points")
    
    
#exit game
def Exit_Game():
    exit()
