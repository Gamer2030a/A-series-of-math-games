import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

canvas_text = canvas.create_text(10, 10, text='', anchor=tk.NW)

test_string = "This is a test"
#Time delay between chars, in milliseconds
delta = 500 
delay = 0
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta

root.mainloop()