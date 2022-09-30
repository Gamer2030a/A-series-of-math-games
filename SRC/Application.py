import tkinter as tk
import customtkinter as ct

# style of root    
ct.set_appearance_mode("System")  # Modes: system (default), light, dark
ct.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Windows 
root = ct.CTk()  # create CTk window like you do with the Tk window
Gamepage = tk.Frame(root)  # Game Page
Startpage = tk.Frame(root) # Start Page

# Copied 
def change_to_newgame():
    newgame_btn.pack_forget()
    Continue_btn.grid_forget()
    Settings_btn.pack_forget()
    Exit_btn.pack_forget()
    
    
    

# Dimension, Icon and Title
root.title("GamesName")
# root.iconbitmap("SRC/rootlication/STTEST.ico")
root.geometry("1280x720")
# Buttons 
def button_NewGame():
    print("button NewGame")
newgame_btn = ct.CTkButton(master=root,width=220, text="NewGame",corner_radius=3,command=change_to_newgame)
# button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
newgame_btn.pack()

def button_Continue():
    print("button Continue")
Continue_btn = ct.CTkButton(master=root,width=220, text="Repository",corner_radius=3, command=button_Continue)
Continue_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

def button_Settings():
    print("button Settings")
Settings_btn = ct.CTkButton(master=root,width=220, text="Settings",corner_radius=3, command=button_Settings)
Settings_btn.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

def button_Exit():
    print("button Exit")
    quit()
Exit_btn = ct.CTkButton(master=root,width=220, text="Exit",corner_radius=3, command=button_Exit)
Exit_btn.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Copyright
copyright = tk.StringVar(value="Game made by Parsa dehghani & Shayan Hosseinzadeh")
label = ct.CTkLabel(master=root,
                               textvariable=copyright,
                               width=145,
                               height=25,
                               corner_radius=0)
label.place(relx=0, rely=1, anchor=tk.SW)


root.mainloop()