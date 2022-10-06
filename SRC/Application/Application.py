import tkinter as tk
from turtle import width
import customtkinter as ct
import pygame
from pygame.locals import *
from pygame import mixer 
import webbrowser
import pyglet
import GameMode
from GameMode import GiveQuestion
from PIL import ImageTk, Image

IsMusicMuted = False


#============== Mute Music Player =============== 
def MuteBGMusic(event):
    event.widget.config(image = Sound_off_img)
    mixer.music.set_volume(0)
    IsMusicMuted = True
#==================================================
def UnmuteBGMusic(event):
    event.widget.config(image = Sound_on_img)
    mixer.music.set_volume(1)
    IsMusicMuted = False
#=====================================================
def switchMusic(event):
    global IsMusicMuted
     
    # Determine is on or off
    if IsMusicMuted:
        print("Unmuted the music")
        UnmuteBGMusic(event)
        IsMusicMuted = False
    else:
        print("Muted the music")
        MuteBGMusic(event)
        IsMusicMuted = True
#=====================================================
#============== Repository Button =============== 
def OpenRepository():
    webbrowser.open('https://github.com/Gamer2030a/A-series-of-math-games.git', new=2)

#================================================

#============== Style of root =============== 
ct.set_appearance_mode("System")  # Modes: system (default), light, dark
ct.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
#============================================

# Windows 
root = ct.CTk()  # create CTk window like you do with the Tk window
root.resizable(width=False, height=False) 

# active music
GameMode.PlayBGMusic()

#================= New Game Button =================================
def change_to_newgame():
    btn_frame.place_forget() 
    Title_1.place_forget()
    Title_2.place_forget()
    Label_frame = tk.Frame(root)
    NewText = GiveQuestion() #to generate the question
    strippedText = str(NewText).replace('(','').replace(')','').replace(',','').replace("'",'')
    Screen_label = ct.CTkLabel(Label_frame,bg_color="#1d1d1d",width=2020,height=220,text=strippedText,text_color="#FFD700",text_font=('Arial',20)).grid(row = 0, column = 0)
    btn_frames = tk.Frame(root,bg="#222325") 
    NumberOne_Btn = ct.CTkButton(btn_frames, text = "1",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1,padx = 3, pady=3)
    NumberTwo_Btn = ct.CTkButton(btn_frames, text = "2",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 0, column = 2,padx = 3, pady=3)
    NumberThree_Btn = ct.CTkButton(btn_frames, text = "3",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 0, column = 3,padx = 3, pady=3)
    NumberFour_Btn = ct.CTkButton(btn_frames, text = "4",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 1, column = 1,padx = 3, pady=3)
    NumberFive_Btn = ct.CTkButton(btn_frames, text = "5",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 1, column = 2,padx = 3, pady=3)
    NumberSix_Btn = ct.CTkButton(btn_frames, text = "6",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 1, column = 3,padx = 3, pady=3)
    NumberSeven_Btn = ct.CTkButton(btn_frames, text = "7",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 2, column = 1,padx = 3, pady=3)
    NumberEight_Btn = ct.CTkButton(btn_frames, text = "8",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 2, column = 2,padx = 3, pady=3)
    NumberNine_Btn = ct.CTkButton(btn_frames, text = "9",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 2, column = 3,padx = 3, pady=3)
    NumberZero_Btn = ct.CTkButton(btn_frames, text = "0",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame).grid(row = 3, column = 2,padx = 3, pady=3)
    Label_frame.place(relx = 0.5, rely=0.14,anchor="center")
    btn_frames.place(relx = 0.5, rely=0.85,anchor="center")
#====================================================================


#========================Settings Button =============================
def change_to_settings():
    btn_frame.place_forget() 
    Title_1.place_forget()
    Title_2.place_forget()
    mute_btn_label.place(relx = 0.5, rely = 0.6 ,anchor = tk.CENTER)
    setting_title = ct.CTkLabel(root, text = "Settings", text_font=('Excluded',30),corner_radius=3)
    setting_title.place(rely = 0.3, relx = 0.5,anchor = tk.CENTER)
    ###############
    def setvolume():
        global volume_slider
        value = volume_slider.cget()
        mixer.music.set_volume(value)  
    volume_slider = tk.Scale(master = root, from_=0, to=100, command=setvolume(), border_color="#206AA5", button_color="White",button_hover_color="black")
    volume_slider.place(relx = 0.5, rely = 0.7, anchor =tk.CENTER)
    #========Buttons =========== 
# Dimension, Icon and Title
root.title("GamesName")
root.iconbitmap(r'SRC\Application\STTEST.ico')
root.geometry("1280x720")
pyglet.font.add_file(r'SRC\Assets\Fonts\Excluded.ttf')

#==============================First Page==============================
#Buttons
btn_frame = tk.Frame(root,bg="#222325", width = 200) 
Newgame_btn = ct.CTkButton(btn_frame, text = "New Game",corner_radius=3,width=300,height= 40,text_font=('Excluded',15), hover=True, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
Repository_btn = ct.CTkButton(btn_frame, text = "Repository",corner_radius=3,width=300,height= 40,text_font=('Excluded',15),command = OpenRepository).grid(row = 2, column = 1, pady=3)
Settings_btn = ct.CTkButton(btn_frame, text = "Settings",corner_radius=3,width=300,height= 40,text_font=('Excluded',15),command = change_to_settings).grid(row = 1, column = 1, pady=3)
exit_btn = ct.CTkButton(btn_frame, text = "Exit",corner_radius=3,width=300,height= 40,command = GameMode.Exit_Game,text_font=('Excluded',15)).grid(row = 3, column = 1, pady=3)
btn_frame.place(relx = 0.5, rely=0.85, anchor =tk.CENTER)
#Title
Title_1 = ct.CTkLabel(master = root, text="Welcome to", width = 300, height= 150, text_font = ('Excluded, 30'))
Title_1.place(rely = 0.32 , relx = 0.43, anchor = tk.CENTER)
Title_2 = tk.Label(root, text="My game", width = 7, height= 5,fg = "Yellow", bg ="#212325" ,font = ('Excluded, 30'))
Title_2.place(rely = 0.32 , relx = 0.59, anchor = tk.CENTER)   
#===================Mute & Unmute Button Configuration=============
Sound_on_img = tk.PhotoImage(file = r'SRC/Assets/Icons/unmute.png',master =root) # Size should be 64*64
Sound_off_img = tk.PhotoImage(file =r'SRC/Assets/Icons/mute.png',master =root)
Mute_btn_frame = tk.Frame(root,bg="#212325",width=68,height=100)
Mute_btn_frame.place(relx = 0.5, rely = 0.6,anchor = tk.CENTER)
mute_btn_label = tk.Label(Mute_btn_frame, image=(Sound_on_img),bg = "#212325",)
mute_btn_label.bind("<Button-1>",switchMusic)
#=================================================================

#=============Copy Right============
copyright = tk.StringVar(value="Game made by Parsa dehghani & Shayan Hosseinzadeh")
label = ct.CTkLabel(master=root,
                               textvariable=copyright,
                               width=145,
                               height=25,
                               corner_radius=0)
label.place(relx=0, rely=1, anchor=tk.SW)
#======================================
#============================================================================




root.mainloop()