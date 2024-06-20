from tkinter import *
from tkinter import ttk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import database

# Function to handle page hopping
def pageHop():
    selectedPage = chosenOption.get()
    if selectedPage == "Topics":
        messagebox.showinfo("Selection Error", "Please select a valid topic.")
        return

    print(f"Welcome to your selected page: {selectedPage}")
    win.destroy()
    try:
        subprocess.run(["python", f"GitBash Folder/{selectedPage}.py"], check=True)
    #If error when trying to find/open a file then this would result
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to open {selectedPage}.py")

# Creating a window
win = Tk()
win.title("User Info")
win.geometry("400x200")

# Creating frames 
topFrame = ttk.Frame(win, padding="10")
topFrame.grid(row=0, column=0, sticky="EW")
frame2 = ttk.Frame(win, padding="10")
frame2.grid(row=1, column=0, sticky="EW")

# Adding padding to the main window
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

# Image/Logo
try:
    image = Image.open(r"C:\Users\64223\OneDrive\Pictures\DDT logo.png")
    img = image.resize((50, 50))
    imgTk = ImageTk.PhotoImage(img)
    imgLabel = Label(topFrame, image=imgTk)
    imgLabel.grid(row=0, column=0, padx=(0, 10), pady=10)
except FileNotFoundError:
    imgLabel = Label(topFrame, text="Logo not found")
    imgLabel.grid(row=0, column=0, padx=(0, 10), pady=10)

# User Info Label
getUser()
userInfo = Label(topFrame, text=f"{user[0]}", font=("Arial", 16))
userInfo.grid(row=0, column=1, padx=10, pady=10, sticky="E")

# Create a StringVar for the chosen option
chosenOption = StringVar()
chosenOption.set("Topics")

# Create a list of items for topics
topics = ["Topics", "English", "Mathematic", "Science", "Social Studies", "ETC"]

# Option menu for topics
optionMenu = ttk.OptionMenu(frame2, chosenOption, *topics)
optionMenu.grid(row=0, column=0, padx=10, pady=10, sticky="W")

# Search Bar
searchBar = ttk.Entry(frame2, width=30)
searchBar.grid(row=0, column=1, padx=10, pady=10, sticky="W")

# Search Button
searchButton = ttk.Button(frame2, text="Search", command=pageHop)
searchButton.grid(row=0, column=2, padx=10, pady=10, sticky="W")

# Run the main window loop
win.mainloop()
