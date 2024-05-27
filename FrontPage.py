# FrontPage.py
from tkinter import *
from tkinter import messagebox
import database

def login():
    username = un.get()
    password = pw.get()

    user = database.getUser(username)
    if user:
        if user[1] == password:
            messagebox.showinfo("Login", "Login Success")
            win.destroy()
            homePage()
        else:
            messagebox.showerror("Login Error", "Incorrect Password")
    else:
        messagebox.showerror("Login Error", "Username not found")

def homePage():
    import homePage
    homePage.show()
def register():
    win.destroy()
    import Register
    Register.show()
    
def show():
    global win, un, pw
    win = Tk()
    win.title("Login")
    win.geometry("300x200")

    Label(win, text="UserName").place(x=10, y=10)
    Label(win, text="Password").place(x=10, y=40)

    un = Entry(win)
    un.place(x=140, y=10)
    pw = Entry(win)
    pw.place(x=140, y=40)
    pw.config(show="*")

    Button(win, text="Login", command=login, height=3, width=20).place(x=10, y=80)
    Button(win, text="Register", command=register, height=3, width=20).place(x=10, y=120)

    win.mainloop()

if __name__ == "__main__":
    show()