import random,time,datetime
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
    
    GameModes = ["Multiply", "Divide", "Subtract" , "Add"]
    CurrentMode = random.choice(GameModes) 
    def GameModeSelect(CurrentMode):
        if CurrentMode == "Multiply":
            return Multiply(NumberOne,NumberTwo)
        elif CurrentMode == "Divide":
            return Divide(NumberOne,NumberTwo)
        elif CurrentMode == "Subtract":
            return Subtract(NumberOne,NumberTwo)
        else:
            return Add(NumberOne,NumberTwo)
    return GameModeSelect(CurrentMode)

    
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
        NumberOne =  random.randint(0,50)
        NumberTwo = random.randint(0,50)
        print(NumberOne)
        print(NumberTwo)
        return Random(NumberOne,NumberTwo)

    elif GameDifficulty == 1:
        print("Medium Question")
        NumberOne =  random.randint(0,100)
        NumberTwo = random.randint(0,100)
        print(NumberOne)
        print(NumberTwo)
        return Random(NumberOne,NumberTwo)

    elif GameDifficulty == 2:
        print("Hard Question")
        NumberOne =  random.randint(0,250)
        NumberTwo = random.randint(0,250)
        print(NumberOne)
        print(NumberTwo)
        return Random(NumberOne,NumberTwo)

    else:
        print("Nightmare Question")
        NumberOne =  random.randint(0,450)
        NumberTwo = random.randint(0,450)
        print(NumberOne)
        print(NumberTwo)
        return Random(NumberOne,NumberTwo)

def ChangeDifficulty(NewGameDifficulty):
    GameDifficulty = NewGameDifficulty
    print("Current game difficulty is " , str(GameDifficulty))
#==============  GameTimer   ===============
def GameTimer(Minutes, Seconds):
    TotalTimeLeft = Minutes * 60 + Seconds
    while TotalTimeLeft > 0:
        timer = datetime.timedelta(seconds = TotalTimeLeft)
        time.sleep(1)
        TotalTimeLeft -= 1
        return TotalTimeLeft # we will return it for the timer to display it at the top of the page 
    print("Total Time Left is 0")
    GameOver
#==============   GameOver   ===============
def GameOver():
    #we will calculate total points and move to a new page for the score
    print("Game Over")

#===========================================
     
global CurrentPlayerPoints
CurrentPlayerPoints = 0

def SavePlayeroints(PlayerAwardedPoints):
    CurrentPlayerPoints = CurrentPlayerPoints + PlayerAwardedPoints
    print("Current Player points are: " , str(CurrentPlayerPoints))
    
    
#exit game
def Exit_Game():
    exit()
