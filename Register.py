# Register.py
from tkinter import *
from tkinter import messagebox
import database

def register():
    username = un.get()
    password = pw.get()
    email = email_entry.get()
    if not username or not password or not email:
        print("All fields are required.")
        return
    # Ensure the table exists
    database.createTable()
    # Inserts user details
    database.insertUser(username, password, email)
    print(f"User {username} registered successfully!")
    
    #Boolean check to see if the user has inputed their details and if not then the error would pop up
    if username and password and email:
        messagebox.showinfo("Registration", "Thank you for registering")
        win.destroy()
        loginPage()
    else:
        messagebox.showwarning("Input Error", "All fields are required")

def loginPage():
    import loginPage
    loginPage.show()

def show():
    global win, un, pw, email_entry
    win = Tk()
    win.title("Register")
    win.geometry("300x200")

    Label(win, text="UserName").place(x=10, y=10)
    Label(win, text="Password").place(x=10, y=40)
    Label(win, text="Email").place(x=10, y=70)

    un = Entry(win)
    un.place(x=140, y=10)
    pw = Entry(win)
    pw.place(x=140, y=40)
    email_entry = Entry(win)
    email_entry.place(x=140, y=70)

    Button(win, text="Register", command=register,height=3, width=20).place(x=10, y=120)

    win.mainloop()

if __name__ == "__main__":
    show()