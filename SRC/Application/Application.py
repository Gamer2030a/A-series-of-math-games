from asyncio.windows_events import NULL
import tkinter as tk
from tkinter.ttk import Button, Widget
from turtle import width
import customtkinter as ct
import pygame
from pygame.locals import *
from pygame import mixer 
import webbrowser
import pyglet
import GameMode
from GameMode import ChangeDifficulty

#============difficulty_radio ============

def radiobutton_event():
    global diff_level
    print("Diffculty changed, current mode: ", difficulty_radio.get())
    diff_level = difficulty_radio.get()
    ChangeDifficulty(diff_level)
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
def BackButton_settings(self):
    Mute_btn_frame.place(anchor = tk.NW)
    mute_btn_label.place(anchor = tk.NW)
    setting_mainframe.place_forget()
    setting_title.place_forget()
    Title_1.place(rely = 0.32 , relx = 0.43, anchor = tk.CENTER)
    Title_2.place(rely = 0.32 , relx = 0.59, anchor = tk.CENTER)
    btn_frame.place(relx = 0.5, rely=0.85, anchor =tk.CENTER)
    Newgame_btn.grid(row = 0, column = 1, pady=3)
    Repository_btn.grid(row = 2, column = 1, pady=3)
    Settings_btn.grid(row = 1, column = 1, pady=3)
    exit_btn.grid(row = 3, column = 1, pady=3)
    Back_Icon.place_forget()

# Windows 
root = ct.CTk()  # create CTk window like you do with the Tk window
root.resizable(width=False, height=False) 
difficulty_radio = tk.IntVar()   
# active music
GameMode.PlayBGMusic()
Icon_path = tk.PhotoImage(file = "SRC\\Assets\\Icons\\back.png")
Back_Icon = tk.Label(root, image = (Icon_path), bg ="#212325")

def BackButton_NewGame(self):
    Mute_btn_frame.place(anchor = tk.NW)
    mute_btn_label.place(anchor = tk.NW)
    Back_Icon.place_forget()
    Screen_label.grid_forget()
    Label_frame.config(bg="#212325")
    NumberOne_Btn.grid_forget()
    NumberTwo_Btn.grid_forget()
    NumberThree_Btn.grid_forget()
    NumberFour_Btn.grid_forget()
    NumberFive_Btn.grid_forget()
    NumberSix_Btn.grid_forget()
    NumberSeven_Btn.grid_forget()
    NumberEight_Btn.grid_forget()
    NumberNine_Btn.grid_forget()
    NumberZero_Btn.grid_forget()
    Title_1.place(rely = 0.32 , relx = 0.43, anchor = tk.CENTER)
    Title_2.place(rely = 0.32 , relx = 0.59, anchor = tk.CENTER)
    btn_frame.lift()
    btn_frame.place(relx = 0.5, rely=0.85, anchor =tk.CENTER)
    
    

#================= New Game Button =================================
def change_to_newgame():
    global NumberOne_Btn
    global NumberTwo_Btn
    global NumberThree_Btn
    global NumberFour_Btn
    global NumberFive_Btn
    global NumberSix_Btn
    global NumberSeven_Btn
    global NumberEight_Btn
    global NumberNine_Btn
    global NumberZero_Btn
    global Screen_label
    global Label_frame
    Back_Icon.bind("<Button-1>",BackButton_NewGame)
    btn_frame.place_forget() 
    Title_1.place_forget()
    Title_2.place_forget()
    Label_frame = tk.Frame(root)
    NewText = GameMode.GiveQuestion() #to generate the question
    strippedText = str(NewText).replace('(','').replace(')','').replace(',','').replace("'",'')
    Screen_label = ct.CTkLabel(Label_frame,bg_color="#1d1d1d",width=2020,height=220,text=strippedText,text_color="#FFD700",text_font=('Arial',20))
    Screen_label.grid(row = 0, column = 0)
    btn_frames = tk.Frame(root,bg="#222325") 
    NumberOne_Btn = ct.CTkButton(btn_frames, text = "1",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberOne_Btn.grid(row = 0, column = 1,padx = 3, pady=3)
    NumberTwo_Btn = ct.CTkButton(btn_frames, text = "2",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberTwo_Btn.grid(row = 0, column = 2,padx = 3, pady=3)
    NumberThree_Btn = ct.CTkButton(btn_frames, text = "3",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberThree_Btn.grid(row = 0, column = 3,padx = 3, pady=3)
    NumberFour_Btn = ct.CTkButton(btn_frames, text = "4",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberFour_Btn.grid(row = 1, column = 1,padx = 3, pady=3)
    NumberFive_Btn = ct.CTkButton(btn_frames, text = "5",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberFive_Btn.grid(row = 1, column = 2,padx = 3, pady=3)
    NumberSix_Btn = ct.CTkButton(btn_frames, text = "6",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberSix_Btn.grid(row = 1, column = 3,padx = 3, pady=3)
    NumberSeven_Btn = ct.CTkButton(btn_frames, text = "7",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberSeven_Btn.grid(row = 2, column = 1,padx = 3, pady=3)
    NumberEight_Btn = ct.CTkButton(btn_frames, text = "8",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberEight_Btn.grid(row = 2, column = 2,padx = 3, pady=3)
    NumberNine_Btn = ct.CTkButton(btn_frames, text = "9",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberNine_Btn.grid(row = 2, column = 3,padx = 3, pady=3)
    NumberZero_Btn = ct.CTkButton(btn_frames, text = "0",text_font=('Excluded',20),corner_radius=3, command=change_to_newgame)
    NumberZero_Btn.grid(row = 3, column = 2,padx = 3, pady=3)
    Back_Icon.config(bg = "#1d1d1d")
    Back_Icon.pack(anchor = tk.NW)
    Back_Icon.lift()
    Label_frame.place(relx = 0.5, rely=0.14,anchor="center")
    Back_Icon.place(anchor = tk.NW)
    btn_frames.place(relx = 0.5, rely=0.85,anchor="center")

#====================================================================


#========================Settings Button =============================
def change_to_settings():
    global setting_mainframe
    global setting_title
    btn_frame.place_forget() 
    Back_Icon.config(bg="#212325")
    Title_1.place_forget()
    Title_2.place_forget()
    Mute_btn_frame.place_forget()
    mute_btn_label.place_forget()
    Back_Icon.bind("<Button-1>",BackButton_settings)
    Back_Icon.place(anchor = tk.NW)
    setting_title = ct.CTkLabel(root, text = "Settings", text_font=('Excluded',30),corner_radius=3)
    setting_title.place(rely = 0.54, relx = 0.5,anchor = tk.CENTER)
    setting_mainframe = ct.CTkFrame(master = root, height= 250, width= 400,fg_color="#222325", border_color="#206AA5", border_width=3)
    setting_mainframe.place(rely = 0.77, relx = 0.5,anchor =tk.CENTER)
    Mute_btn_label1 = ct.CTkButton(setting_mainframe, text = "Mute Music",width=140,height=50, text_font=('Excluded',14),hover_color="red",fg_color="green",command =switchMusic)
    Mute_btn_label1.place(anchor=tk.CENTER, relx = 0.5, rely = 0.17)
    Mute_sfx_btn = ct.CTkButton(setting_mainframe, text = "Mute SFX",width=148,height=50, text_font=('Excluded',14),hover_color="red",fg_color="green")
    Mute_sfx_btn .place(anchor=tk.CENTER, relx = 0.5, rely = 0.41)
    vol_title = ct.CTkLabel(setting_mainframe, text = "Volume", text_font = ('Excluded',13))
    vol_title.place(anchor=tk.CENTER, relx = 0.5, rely = 0.59)
    vol_slider = ct.CTkSlider(setting_mainframe, from_=0.0, to= 1.0)
    current_vol = vol_slider.get()
    vol_slider.place(anchor=tk.CENTER, relx = 0.5, rely = 0.67)
    #====================Difficulty Levels =====================
    Difficulty_title = ct.CTkLabel(setting_mainframe, text = "Difficulty", text_font = ('Excluded',14))
    Difficulty_title.place(anchor=tk.CENTER, relx = 0.5, rely = 0.78)
    Easy_difficulty_chck = ct.CTkRadioButton(setting_mainframe, text = "Easy", hover=True, command = radiobutton_event, variable=difficulty_radio, value=0)
    Easy_difficulty_chck.place(anchor=tk.CENTER, relx = 0.2, rely = 0.89)
    Normal_difficulty_chck = ct.CTkRadioButton(setting_mainframe, text = "Normal", hover=True,command = radiobutton_event, variable=difficulty_radio, value=1)
    Normal_difficulty_chck.place(anchor=tk.CENTER, relx = 0.4, rely = 0.89)
    Hard_difficulty_chck = ct.CTkRadioButton(setting_mainframe, text = "Hard", hover=True,command = radiobutton_event, variable=difficulty_radio, value=2)
    Hard_difficulty_chck.place(anchor=tk.CENTER, relx = 0.6, rely = 0.89)
    Nightmare_difficulty_chck = ct.CTkRadioButton(setting_mainframe, text = "Nightmare", hover=True,command = radiobutton_event, variable=difficulty_radio, value=3)
    Nightmare_difficulty_chck.place(anchor=tk.CENTER, relx = 0.8, rely = 0.89)
    



#=========================================================
# Dimension, Icon and Title
root.title("GamesName")
root.iconbitmap(r'SRC\Application\STTEST.ico')
root.geometry("1280x720")
pyglet.font.add_file(r'SRC\Assets\Fonts\Excluded.ttf')

#==============================First Page==============================
#Buttons
btn_frame = tk.Frame(root,bg="#222325", width = 200) 
Newgame_btn = ct.CTkButton(btn_frame, text = "New Game",corner_radius=3,width=300,height= 40,text_font=('Excluded',15), hover=True, command=change_to_newgame)
Newgame_btn.grid(row = 0, column = 1, pady=3)
Repository_btn = ct.CTkButton(btn_frame, text = "Repository",corner_radius=3,width=300,height= 40,text_font=('Excluded',15),command = OpenRepository)
Repository_btn.grid(row = 2, column = 1, pady=3)
Settings_btn = ct.CTkButton(btn_frame, text = "Settings",corner_radius=3,width=300,height= 40,text_font=('Excluded',15),command = change_to_settings)
Settings_btn.grid(row = 1, column = 1, pady=3)
exit_btn = ct.CTkButton(btn_frame, text = "Exit",corner_radius=3,width=300,height= 40,command = GameMode.Exit_Game,text_font=('Excluded',15))
exit_btn.grid(row = 3, column = 1, pady=3)
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
Mute_btn_frame.place(anchor = tk.NW)
mute_btn_label = tk.Label(Mute_btn_frame, image=(Sound_on_img),bg = "#212325",)
mute_btn_label.bind("<Button-1>",switchMusic)
mute_btn_label.place(anchor = tk.NW)
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