import tkinter as tk
from tkinter import ttk

# Initialize main window
root = tk.Tk()
root.title("HomePage")
root.geometry("800x600")

# Define styles
style = ttk.Style()
style.configure("TFrame", background="white")
style.configure("TButton", padding=6)
style.configure("TLabel", padding=6)

#Page Navigation
import subprocess
from tkinter import messagebox

class PageNavigator:
    def __init__(self, window, option_var):
        self.win = window
        self.chosenOption = option_var

    def pageHop(self):
        selectedPage = self.chosenOption.get()
        if selectedPage == "Topics":
            messagebox.showinfo("Selection Error", "Please select a valid topic.")
            return
        # Giving a text response to the input of the user
        print(f"Welcome to your selected page: {selectedPage}")
        self.win.destroy()
        try:
            subprocess.run(["python", f"GitBash Folder/{selectedPage}.py"], check=True)
        # If error when trying to find/open a file then this would result
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to open {selectedPage}.py")


# Create frames for each section
userInfoFrame = ttk.Frame(root, width=200, height=100, relief="solid", padding=10)
userInfoFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

imagePlaceholderFrame = ttk.Frame(root, width=400, height=100, relief="solid", padding=10)
imagePlaceholderFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

topicsDropdownFrame = ttk.Frame(root, width=200, height=50, relief="solid", padding=10)
topicsDropdownFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

searchBarFrame = ttk.Frame(root, width=400, height=50, relief="solid", padding=10)
searchBarFrame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

historyFrame = ttk.Frame(root, width=600, height=200, relief="solid", padding=10)
historyFrame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

descriptionFrame = ttk.Frame(root, width=600, height=100, relief="solid", padding=10)
descriptionFrame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

audioPlayerFrame = ttk.Frame(root, width=600, height=50, relief="solid", padding=10)
audioPlayerFrame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Add widgets to the frames
userInfoButton = ttk.Button(userInfoFrame, text="User Info")
userInfoButton.pack(expand=True)

imagePlaceholderLabel = ttk.Label(imagePlaceholderFrame, text="Image Placeholder")
imagePlaceholderLabel.pack(expand=True)

topicsLabel = ttk.Label(topicsDropdownFrame, text="Topics")
topicsLabel.pack(side="left")
topicsCombo = ttk.Combobox(topicsDropdownFrame, values=["Topic 1", "Topic 2", "Topic 3"])
topicsCombo.pack(side="left", expand=True)

searchEntry = ttk.Entry(searchBarFrame)
searchEntry.pack(side="left", expand=True, fill="x")
searchButton = ttk.Button(searchBarFrame, text="🔍")
searchButton.pack(side="left")

historyLabel = ttk.Label(historyFrame, text="History")
historyLabel.pack(anchor="w")
historyList = tk.Listbox(historyFrame)
historyList.insert(1, "Question 3")
historyList.insert(2, "Question 2")
historyList.insert(3, "Question 1")
historyList.pack(expand=True, fill="both")

descriptionLabel = ttk.Label(descriptionFrame, text="Description of KnowLed and its features")
descriptionLabel.pack(expand=True, fill="both")

audioPlayerLabel = ttk.Label(audioPlayerFrame, text="Audio Player")
audioPlayerLabel.pack(side="left")
audioPlayer = ttk.Button(audioPlayerFrame, text="Play")
audioPlayer.pack(side="left")

# Run the application
root.mainloop()
