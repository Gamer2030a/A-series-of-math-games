from tkinter import *
import customtkinter
def raise_frame(frame):
    frame.tkraise()

root = Tk()

StartPage = Frame(root)
GamePage = Frame(root)
# f3 = Frame(root)
# f4 = Frame(root)

for frame in (StartPage, GamePage):
    frame.grid(row=0, column=0, sticky='news')

Button(StartPage, text='New Game', command=lambda:raise_frame(GamePage)).pack()
Label(GamePage, text='Game Page').pack()

# Label(f2, text='FRAME 2').pack()
# Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

# Label(f3, text='FRAME 3').pack(side='left')
# Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

# Label(f4, text='FRAME 4').pack()
# Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(StartPage)
root.mainloop()