from tkinter import *
from tkinter import ttk, messagebox
from database import saveArticle
import homePage

def show(username):
    def save():
        # Strip so that no whitespace is there e.g. "  " unnecessary empty space between string
        title = titleEntry.get().strip()
        # the 1.0 is the size of the text
        content = contentText.get("1.0", END).strip()
        if title and content:
            try:
                saveArticle(title, content)
                messagebox.showinfo("Success", "Article saved successfully!")
                win.destroy()
                homePage.show(username)  # Passes the username to homePage.show()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Title and content cannot be empty.")

    def home():
        win.destroy()
        homePage.show(username)  # Passes the username to homePage.show()

    win = Toplevel()
    win.title("Article Creation")
    win.geometry("800x700")

    # Entry for the article title
    titleLabel = Label(win, text="Title:")
    titleLabel.pack(pady=10)

    titleEntry = Entry(win, width=50)
    titleEntry.pack(pady=10)

    # Entry area for content or typed up information
    contentLabel = Label(win, text="Content:")
    contentLabel.pack(pady=10)

    contentText = Text(win, wrap="word", width=70, height=15)
    contentText.pack(pady=10)

    # Frame for buttons to manage layout
    buttonFrame = Frame(win)
    buttonFrame.pack(pady=10)

    # Save and Home Buttons for linking and page hopping
    saveButton = Button(buttonFrame, text="Save Article", command=save)
    saveButton.pack(side=LEFT, padx=5)

    homeButton = Button(buttonFrame, text="Back Home", command=home)
    homeButton.pack(side=LEFT, padx=5)

    win.mainloop()
