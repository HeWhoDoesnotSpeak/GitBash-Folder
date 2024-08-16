from tkinter import *
from tkinter import messagebox
import database
import homePage

# The function for login page which includes entry inputs expections for errors, checkers for username and password.
def login():
    username = un.get().strip()
    password = pw.get().strip()

    if not username or not password:
        messagebox.showerror("Login Error", "No blanks allowed")
        return

    user = database.getUser(username)
    if user:
        if user[1] == password:
            messagebox.showinfo("Login", "Login Success")
            win.destroy()
            # Passes the username to homePage.show()
            homePage.show(username)  
        else:
            messagebox.showerror("Login Error", "Incorrect Password")
    # Makes sure the username isn't already registered for a login
    else:
        allUsers = database.getAllUsers()
        if username not in [user[0] for user in allUsers]:
            messagebox.showerror("Login Error", "Username not found")
        else:
            messagebox.showerror("Login Error", "Incorrect Username and Password")

# Page hopping stuff
def register():
    import register
    win.destroy()
    register.show()

# Label and button set up for with the window size and entry labels
def show():
    global win, un, pw
    win = Tk()
    win.title("Login")
    win.geometry("400x400")

    Label(win, text="Sign In", font=("Arial", 20)).pack(pady=10)
    
    Label(win, text="User Name:").place(x=50, y=80)
    un = Entry(win, width=30)
    un.place(x=150, y=80)
    
    Label(win, text="Password:").place(x=50, y=120)
    pw = Entry(win, show="*", width=30)
    pw.place(x=150, y=120)

    Button(win, text="Log in", command=login, width=15).place(x=100, y=160)
    Button(win, text="Register", command=register, width=15).place(x=200, y=160)

    win.mainloop()
    

if __name__ == "__main__":
    show()
