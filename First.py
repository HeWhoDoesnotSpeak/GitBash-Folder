import subprocess
from tkinter import *

top=Tk()
top.geometry("400x400")
def second():
    print("killing first")
    top.destroy()
    subprocess.run(["python","GitBash Folder//second.py"])

B=Button(top,text="go to sec", command=second)
B.pack()

top.mainloop()