
import subprocess
from tkinter import messagebox

class pageNavigator:
    def __init__(self, window, option_var):
        self.win = window
        self.chosenOption = option_var

    def pageHop(self):
        selectedPage = self.chosenOption.get()
        if selectedPage == "Topics":
        # Giving a text response to the input of the user
            print(f"Welcome to your selected page: {selectedPage}")
        try:
            subprocess.run(["python", f"GitBash Folder/{selectedPage}.py"], check=True)
            self.win.destroy()
        # If error occurs when trying to find or open a file then this would result
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to open {selectedPage}.py")
