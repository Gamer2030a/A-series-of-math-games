import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("GamesName")
app.iconbitmap("SRC/Application/STTEST.ico")
app.geometry("1280x720")

def button_NewGame():
    print("button NewGame")
button = customtkinter.CTkButton(master=app,width=220, text="NewGame",corner_radius=3, command=button_NewGame)
button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

def button_Continue():
    print("button Continue")
button = customtkinter.CTkButton(master=app,width=220, text="Repository",corner_radius=3, command=button_Continue)
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

def button_Settings():
    print("button Settings")
button = customtkinter.CTkButton(master=app,width=220, text="Settings",corner_radius=3, command=button_Settings)
button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

def button_Exit():
    print("button Exit")
button = customtkinter.CTkButton(master=app,width=220, text="Exit",corner_radius=3, command=button_Exit)
button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

app.mainloop()