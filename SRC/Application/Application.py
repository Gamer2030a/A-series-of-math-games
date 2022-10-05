import tkinter as tk
import customtkinter as ct
import pygame
from pygame.locals import *
from pygame import mixer
import pyglet
import GameMode

#============== Mute Music Player =============== 
def MuteBGMusic():
    Mute_btn.config(image = Sound_off_img)
    mixer.music.stop()       
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
    Screen_label = ct.CTkLabel(Label_frame,bg_color="#1d1d1d",width=2020,height=220,text="what is 2*2?",text_color="#FFD700",text_font=('Arial',20)).grid(row = 0, column = 0)
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

# Dimension, Icon and Title
root.title("GamesName")
root.iconbitmap(r'SRC\Application\STTEST.ico')
root.geometry("1280x720")
pyglet.font.add_file(r'SRC\Assets\Fonts\Excluded.ttf')

#==============================First Page==============================
#Buttons
btn_frame = tk.Frame(root,bg="#222325", width = 200) 
Newgame_btn = ct.CTkButton(btn_frame, text = "New Game",corner_radius=3,width=300,height= 40,text_font=('Excluded',15), hover=True, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
Repository_btn = ct.CTkButton(btn_frame, text = "Repository",corner_radius=3,width=300,height= 40,text_font=('Excluded',15)).grid(row = 2, column = 1, pady=3)
Settings_btn = ct.CTkButton(btn_frame, text = "Settings",corner_radius=3,width=300,height= 40,text_font=('Excluded',15)).grid(row = 1, column = 1, pady=3)
exit_btn = ct.CTkButton(btn_frame, text = "Exit",corner_radius=3,width=300,height= 40,command = GameMode.Exit_Game,text_font=('Excluded',15)).grid(row = 3, column = 1, pady=3)
btn_frame.place(relx = 0.5, rely=0.85, anchor =tk.CENTER)
#Title
Title_1 = ct.CTkLabel(master = root, text="Welcome to", width = 300, height= 150, text_font = ('Excluded, 30'))
Title_1.place(rely = 0.32 , relx = 0.45, anchor = tk.CENTER)
Title_2 = tk.Label(root, text="My game", width = 7, height= 5,fg = "Yellow", bg ="#212325" ,font = ('Excluded, 30'))
Title_2.place(rely = 0.32 , relx = 0.61, anchor = tk.CENTER)   
# Sound on
Sound_on_img = tk.PhotoImage(file = r'SRC\Assets\Icons\unmute.png',master =root) # Size should be 64*64
# Sound Off
Sound_off_img = tk.PhotoImage(file =r'SRC/Assets/Icons/mute.png',master =root)
Mute_btn = tk.Button(root, image=(Sound_on_img), text = "", height=64, width=64, bg="#212325",borderwidth=0,command = MuteBGMusic) # Size should be 64*64
Mute_btn.place(anchor = tk.NW)
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