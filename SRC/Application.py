import tkinter as tk
import customtkinter as ct
from playsound import playsound
import Application.GameMode

# style of root    
ct.set_appearance_mode("System")  # Modes: system (default), light, dark
ct.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Windows 
root = ct.CTk()  # create CTk window like you do with the Tk window

# new game buttn function
def change_to_newgame():
    btn_frame.place_forget() 
    playBtnSound()
    btn_frames = tk.Frame(root,bg="#222325") 
    NumberOne_Btn = ct.CTkButton(btn_frames, text = "1",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberTwp_Btn = ct.CTkButton(btn_frames, text = "2",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberThree_Btn = ct.CTkButton(btn_frames, text = "3",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberFour_Btn = ct.CTkButton(btn_frames, text = "4",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberFive_Btn = ct.CTkButton(btn_frames, text = "5",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberSix_Btn = ct.CTkButton(btn_frames, text = "6",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberSeven_Btn = ct.CTkButton(btn_frames, text = "7",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberEight_Btn = ct.CTkButton(btn_frames, text = "8",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberNine_Btn = ct.CTkButton(btn_frames, text = "9",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    NumberZero_Btn = ct.CTkButton(btn_frames, text = "0",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
    btn_frames.place(relx = 0.45, rely=0.75)

# Dimension, Icon and Title
root.title("GamesName")
root.iconbitmap(r'SRC\Application\STTEST.ico')
root.geometry("1280x720")

def Exit_Game():
    playBtnSound()
    exit()

def playBtnSound():
    playsound('SRC\Assets\SFX\ButtonPing.mp3')

# Buttons 
btn_frame = tk.Frame(root,bg="#222325") 
Newgame_btn = ct.CTkButton(btn_frame, text = "New Game",corner_radius=3, command=change_to_newgame).grid(row = 0, column = 1, pady=3)
Continue_btn = ct.CTkButton(btn_frame, text = "Continue",corner_radius=3).grid(row = 1, column = 1, pady=3)
Repository_btn = ct.CTkButton(btn_frame, text = "Repository",corner_radius=3).grid(row = 2, column = 1, pady=3)
exit_btn = ct.CTkButton(btn_frame, text = "Exit",corner_radius=3,command = Exit_Game).grid(row = 3, column = 1, pady=3)
btn_frame.place(relx = 0.45, rely=0.75)
    
# Copyright
copyright = tk.StringVar(value="Game made by Parsa dehghani & Shayan Hosseinzadeh")
label = ct.CTkLabel(master=root,
                               textvariable=copyright,
                               width=145,
                               height=25,
                               corner_radius=0)
label.place(relx=0, rely=1, anchor=tk.SW)


root.mainloop()