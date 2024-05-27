from tkinter import *
from tkinter import ttk

win = Tk()
win.title("English")
win.geometry("200x200")
topFrame = ttk.Frame(win, padding="10")
topFrame.grid(row=0, column=0, sticky="EW")
l1 = Label(topFrame, text="Is this working?")
l1.grid(column=0, row=0)

win.mainloop()


