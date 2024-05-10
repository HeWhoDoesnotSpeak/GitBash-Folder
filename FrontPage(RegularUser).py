from tkinter import *
import subprocess
from tkinter import ttk

root = Tk()
root.geometry("1000x1000")
def hop():
    print("Entering homepage")
    root.destroy()
    subprocess.run(["python","GitBash Folder//HomePage.py"])

Ebut = Button(root, text="Enter", command = hop, height =10, width= 20, borderwidth=10, pady=10)
Ebut.grid(row=3, column=1)
Ebut.pack()

root.mainloop()
