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
#===========================================

     
   
def SavePlayeroints():
    print("points")
    
    
#exit game
def Exit_Game():
    exit()
