from tkinter import *

root = Tk()
root.geometry("400x400")

myLabel = Label(root, text="This is second page")
myLabel.pack()

print("I'm second")
root.mainloop()