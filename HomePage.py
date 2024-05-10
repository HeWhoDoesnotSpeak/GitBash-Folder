from tkinter import *
from tkinter import ttk
from tkinter import Radiobutton
import subprocess

# Create a window
root = Tk()
root.geometry

# Checkbutton function
def check():
  print(check1_var.get())

#Page Hopping
# Create function that allows for where user clicks to put into the subprocess
def pageHop():
  print("Welcome to your selected page")
  root.destroy()
  subprocess[("python","")]


# Radiobutton function
  

# Create a frame for first 2 widgets
frame1 = ttk.Frame(root)
frame1.grid(row=1, column=0)

#Create a StringVar() to store text
words = StringVar()

title=Label(root, text="KNOWLED")
title.grid(row=0,column=1, sticky="NSEW")
text=Label(root, text="I hate working on design with pixels, this will take a while to put into place")
text.grid(row=4,column=1, sticky="NSEW")

# Create a text entry field
words_entry = ttk.Entry(frame1, textvariable=words)
words_entry.grid(row=2, column=1, padx=10, pady=5, sticky="NSEW")

# Create a frame for the second 2 widgets
frame2 = ttk.Frame(root,)
frame2.grid(row=2, column=1, sticky="NSEW")

# Create a second label with longer text and add it to the window using pack()
label2 = ttk.Label(frame2, textvariable=words, wraplength=150)
label2.grid(row=2, column=1, padx=10, pady=5)

# Create a StringVar() for the chosen option
chosen_option = StringVar()

# Create a list of items for the Option Menu
options = ["Topics","English","Mathematic","Science","Social Studies","ETC"]

# Create the option menu and place in row 3, column 0
option_menu = ttk.OptionMenu(frame2, chosen_option, options[0], *options)
option_menu.grid(row=2, column=1, padx=0, pady=5,sticky="W")

# Create a LabelFrame for the checkbuttons
frame3 = ttk.LabelFrame(root, text="Checkbuttons")
frame3.grid(row=3, column=1, padx=10, pady=10, sticky="EW")

# Create variables for 2 checkbuttons
check1_var = IntVar()
check2_var = IntVar()
check2_var.set(1)

# Create a LabelFrame for the radiobuttons
frame4 = ttk.LabelFrame(root, text="Radiobuttons")
frame4.grid(row=3, column=0, padx=10, pady=10, sticky="WE")

#Create 3 radiobuttons


# Run the main window loop
root.mainloop()
