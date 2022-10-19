import tkinter  
import customtkinter 

def on_change(e):
    print (e.widget.get())
    showlabel.config(text = e.widget.get())

root = tkinter.Tk()

entry = customtkinter.CTkEntry(master=root,
                               placeholder_text="CTkEntry",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


root.mainloop()