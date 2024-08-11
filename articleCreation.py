from tkinter import *
from tkinter import ttk, messagebox
from database import saveArticle
from homePage import show

def show():
    def save():
        title = titleEntry.get().strip()
        # the 1.0 is the size of the text
        content = contentText.get("1.0", END).strip()
        if title and content:
            try:
                saveArticle(title, content)
                messagebox.showinfo("Success", "Article saved successfully!")
                win.destroy()
                show()

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Title and content cannot be empty.")
    def home():
        win.destroy()
        show()

    win = Toplevel()
    win.title("Article Creation")
    win.geometry("800x700")

    titleLabel = Label(win, text="Title:")
    titleLabel.pack(pady=10)

    titleEntry = Entry(win, width=50)
    titleEntry.pack(pady=10)

    contentLabel = Label(win, text="Content:")
    contentLabel.pack(pady=10)

    contentText = Text(win, wrap="word", width=70, height=15)
    contentText.pack(pady=10)

    saveButton = Button(win, text="Save Article", command=save)
    saveButton.pack(pady=10)

    homeButton = Button(win, text="Back Home", command=home)
    homeButton.pack(pady=10)

    win.mainloop()
