from tkinter import *
from tkinter import ttk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import database

# Creating a window
win = Tk()
win.title("Home Page")
win.geometry("1000x1000")

# Define styles
style = ttk.Style()
style.configure("tFrame", background="white")
style.configure("tButton", padding=6)
style.configure("tLabel", padding=6)

# Create a list of items for topics
topics = ["Topics", "English", "Mathematic", "Science", "Social Studies", "ETC"]

# Creating a method of transporting pages
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

# Creating frames (Important)
userInfoFrame = ttk.Frame(win,width=200, height=100, relief="solid", padding=10)
userInfoFrame.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

logoFrame = ttk.Frame(win,width=200, height=100, relief="solid", padding=10)
logoFrame.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")

topicsFrame = ttk.Frame(win,width=200, height=100, relief="solid", padding=10)
topicsFrame.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")

topicsDropdownFrame = ttk.Frame(win, width=200, height=50, relief="solid", padding=10)
topicsDropdownFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

searchBarFrame = ttk.Frame(win,width=200, height=100, relief="solid", padding=10)
searchBarFrame.grid(row=1,column=1,padx=10,pady=10,sticky="nsew")

historyFrame = ttk.Frame(win,width=200, height=100, relief="solid", padding=10)
historyFrame.grid(row=2,column=1,padx=10,pady=10,sticky="nsew")

dpFrame = ttk.Frame(win,width=200, height=100, relief="solid", padding=10)
dpFrame.grid(row=3,column=0,padx=10,pady=10,sticky="nsew")
videoFrame = ttk.Frame(win,width=200, height=100, relief="solid", padding=10)
videoFrame.grid(row=4,column=1,padx=10,pady=10,sticky="nsew")

# Widgets for frames
userInfoButton = ttk.Button(userInfoFrame, text="User Info")
userInfoButton.pack(expand=True)

logoImage = Label(logoFrame, text="Image")

topicsLabel = ttk.Label(topicsDropdownFrame, text="Topics")
topicsLabel.pack(side="left")

topicsCombo = ttk.Combobox(topicsDropdownFrame, values=topics)
topicsCombo.pack(side="left", expand=True)

# Image/Logo
def Logo():
    try:
        image = Image.open(r"C:\Users\64223\OneDrive\Pictures\DDT logo.png")
        img = image.resize((50, 50))
        imgTk = ImageTk.PhotoImage(img)
        imgLabel = Label(logoFrame, image=imgTk)
        imgLabel.grid(row=0, column=2, padx=(0, 10), pady=10, sticky='w'+'e'+'s'+'n')
    except FileNotFoundError:
        imgLabel = Label(logoFrame, text="Logo not found")
        imgLabel.grid(row=0, column=2, padx=(0, 10), pady=10)

# Create a StringVar for the chosen option
chosenOption = StringVar()
chosenOption.set("Topics")

# Option menu for topics
optionMenu = ttk.OptionMenu(topicsFrame, chosenOption, *topics)
optionMenu.grid(row=0, column=0, padx=10, pady=10, sticky="W")

# Search Bar
searchBar = ttk.Entry(searchBarFrame, width=30)
searchBar.grid(row=0, column=1, padx=10, pady=10, sticky="W")

# Search Button
searchButton = ttk.Button(searchBarFrame, text="Search", command=pageHop)
searchButton.grid(row=0, column=2, padx=10, pady=10, sticky="W")

# Run the main window loop
if __name__ == "__main__":
    win.mainloop()
