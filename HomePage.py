from tkinter import *
from tkinter import ttk
from tkinter import Radiobutton
import subprocess
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

# Create a window
win = Tk()
win.geometry("250x100")

#Login details
global e1
global e2

# Page Hopping: Creates a function that allows for where user clicks to put into the subprocess
def pageHop():
  print("Welcome to your selected page")
  win.destroy()
  subprocess[("python","GitBash Folder//"+chosen_option+".py")]
  

# Creating frames 
topFrame = ttk.Frame(win)
topFrame.grid()
frame2 = ttk.Frame(win)
frame2.grid()


# Create a StringVar() to store text
words = StringVar()

#Top Frame
userInfo=Label(topFrame, text="User Info", font=(20))
userInfo.grid(row=0,column=0, sticky="E")

#Image/Logo
image=Image.open(r"C:\Users\64223\OneDrive\Pictures\DDT logo.png")
img=image.resize((30,30))
imgtk=ImageTk.PhotoImage(img)
img1=Label(win, image=imgtk)
img1.grid(row=0, column=1, sticky="W")

# Create a StringVar() for the chosen option
chosen_option = StringVar()

# Create a list of items for topics
topics = ["Topics","English","Mathematic","Science","Social Studies","ETC"]

# Option menu for topics
option_menu = ttk.OptionMenu(frame2, chosen_option, topics[0], *topics)
option_menu.grid(row=0, column=0, padx=0, pady=0,sticky="E")

# Search Bar
searchBar = ttk.Entry(frame2, textvariable=words)
searchBar.grid(row=0, column=1, padx=5, pady=5, sticky="NW")


# Run the main window loop
win.mainloop()
