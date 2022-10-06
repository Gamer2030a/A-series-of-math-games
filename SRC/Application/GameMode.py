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
#==============  GameModes  ===============

def Multiply(NumberOne,NumberTwo):
    print("what is " , str(NumberOne) , " X " , str(NumberTwo) , " ?")
    print (NumberOne*NumberTwo)
    return "what is " , str(NumberOne) , " X " , str(NumberTwo) , " ?"

def Divide(NumberOne,NumberTwo):
    print("what is " , str(NumberOne) , " / " , str(NumberTwo) , " ?")
    return "what is " , str(NumberOne) , " / " , str(NumberTwo) , " ?"

def Subtract(NumberOne,NumberTwo):
    print("what is " , str(NumberOne) , " - " , str(NumberTwo) , " ?")
    return "what is " , str(NumberOne) , " - " , str(NumberTwo) , " ?"
        
def Add(NumberOne,NumberTwo):
    print("what is " , str(NumberOne) , " + " , str(NumberTwo) , " ?")
    return "what is " , str(NumberOne) , " + " , str(NumberTwo) , " ?"

def Random(NumberOne,NumberTwo):
    #had a return 
    random.choice([Multiply(NumberOne,NumberTwo),Divide(NumberOne,NumberTwo),Subtract(NumberOne,NumberTwo),Add(NumberOne,NumberTwo)])
#============== Difficulty  ===============
EasyRange = [0,20]
MediumRange = [0,100]
HardRange = [0,250]
NightmareRange = [0,2500]
# 0 = easy
# 1 = medium
# 2 = hard
# 3 = nightmare

def GiveQuestion():
    global GameDifficulty
    GameDifficulty = 2
    
    if GameDifficulty == 0:
        print("Easy Question")
        return random.randint(0,250) , random.randint(0,250)

    elif GameDifficulty == 1:
        print("Medium Question")
        return random.randint(0,250) , random.randint(0,250)

    elif GameDifficulty == 2:
        print("Hard Question")
        NumberOne =  random.randint(0,250)
        NumberTwo = random.randint(0,250)
        print(NumberOne)
        print(NumberTwo)
        Random(NumberOne,NumberTwo)

    else:
        print("Nightmare Question")
        return random.randint(0,250) , random.randint(0,250)
#===========================================

     
   
def SavePlayeroints():
    print("points")
    
    
#exit game
def Exit_Game():
    exit()
