# loginPage.py
from tkinter import *
from tkinter import messagebox
import database
from homePage import *

#The function for login page
def login():
    username = un.get()
    password = pw.get()

    if not username or not password:
        messagebox.showerror("Login Error", "No Blank allowed")
        return

    user = database.getUser(username)
    if user:
        if user[1] == password:
            messagebox.showinfo("Login", "Login Success")
            win.destroy()
            homePage()
        else:
            messagebox.showerror("Login Error", "Incorrect Password")
    else:
        # Checks if the username exists in the database
        all_users = database.getAllUsers()
        if username not in [user[0] for user in all_users]:
            messagebox.showerror("Login Error", "Username not found")
        else:
            messagebox.showerror("Login Error", "Incorrect Username and Password")

#Page hopping stuff
def homePage():
    import homePage
    homePage.show()
def register():
    win.destroy()
    import register
    register.show()

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
    Button(win, text="register", command=register, height=3, width=20).place(x=10, y=120)

    win.mainloop()

if __name__ == "__main__":
    show()