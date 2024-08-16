from tkinter import *
from tkinter import messagebox
from database import *

def register():
    # Takes the user' sinputs as its information of the id and using confirmation to ensure that the username doesn't already exist and the passwords match
    username = usernameEntry.get().strip()
    password = passwordEntry.get().strip()
    confirmPassword = confirmPasswordEntry.get().strip()
    email = emailEntry.get().strip()

    if not username or not password or not email:
        messagebox.showwarning("Input Error", "All fields are required")
        return

    if password != confirmPassword:
        messagebox.showwarning("Input Error", "Passwords do not match")
        return

    # Ensures the table exists
    createTables()

    # Checks if username already exists within the database using username as the search variable
    if checkUserExists(username):
        messagebox.showinfo("Error", "Username already exists. Please choose a different username.")
        return

    # Checks for username and password length
    if len(username) < 5 or len(username) > 25:
        messagebox.showinfo("Error", "Username must be between 5 and 25 characters")
        return
    elif len(password) < 5 or len(password) > 20:
        messagebox.showinfo("Error", "Password must be between 5 and 20 characters")
        return
    
    # Inserts the user's details into the database with login details
    insertUser(username, password, email)
    print(f"User {username} registered successfully!")
    messagebox.showinfo("Registration", "Thank you for registering")
    win.destroy()
    loginPage()

# Acts as a page hopper function
def loginPage():
    import loginPage
    loginPage.show()

# Label set up of register with global variables and entry so that user input can be saved into the database
def show():
    global win, usernameEntry, passwordEntry, confirmPasswordEntry, emailEntry
    win = Tk()
    win.title("Register")
    win.geometry("400x400")

    Label(win, text="Register", font=("Arial", 20)).pack(pady=10)

    Label(win, text="Email:").place(x=50, y=100)
    emailEntry = Entry(win, width=30)
    emailEntry.place(x=150, y=100)
    
    Label(win, text="Username:").place(x=50, y=140)
    usernameEntry = Entry(win, width=30)
    usernameEntry.place(x=150, y=140)
    
    Label(win, text="Password:").place(x=50, y=180)
    passwordEntry = Entry(win, show="*", width=30)
    passwordEntry.place(x=150, y=180)
    
    Label(win, text="Confirm Password:").place(x=50, y=220)
    confirmPasswordEntry = Entry(win, show="*", width=30)
    confirmPasswordEntry.place(x=150, y=220)

    Button(win, text="Register", command=register, width=15).place(x=150, y=260)

    win.mainloop()

if __name__ == "__main__":
    show()
