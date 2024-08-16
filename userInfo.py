from tkinter import *
from tkinter import ttk, messagebox
from database import *
import homePage

def show(username):
    def updatePassword():
        newPassword = newPasswordEntry.get().strip()
        if newPassword:
            try:
                # Updates the user's password in the database
                updateUserPassword(username, newPassword)
                messagebox.showinfo("Success", "Password updated successfully!")
                # Closes the current window
                win.destroy() 
                # Passes the username to homePage using show()
                homePage.show(username)  
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Password cannot be empty.")

    def goHome():
        # Closes the current window
        win.destroy()  
        # Passes the username to homePage using show()
        homePage.show(username)  

    win = Toplevel()
    win.title("User Info")
    win.geometry("400x300")

    # Fetches and displays the user's info
    user = getUser(username)
    if user:
        # Displays the user's username
        userLabel = Label(win, text=f"Username: {user[0]}")  
        userLabel.pack(pady=10)
        # Displays the user's email
        emailLabel = Label(win, text=f"Email: {user[2]}")  
        emailLabel.pack(pady=10)

        # Displays the original password which is then masked using hashkey
        passwordLabel = Label(win, text=f"Current Password: {'*' * len(user[1])}")
        passwordLabel.pack(pady=10)

        # The input entry for the new password
        newPasswordLabel = Label(win, text="New Password:")
        newPasswordLabel.pack(pady=10)
        newPasswordEntry = Entry(win, show="*", width=50)
        newPasswordEntry.pack(pady=10)

        # The confirmation button to update the password
        updateButton = Button(win, text="Update Password", command=updatePassword)
        updateButton.pack(pady=10)

        # Home button to navigate back to homePage
        homeButton = Button(win, text="Home", command=goHome)
        homeButton.pack(pady=10)
    else:
        messagebox.showerror("Error", "User not found.")
        # Closes the window if user not found
        win.destroy()
        # Redirects back home if user is not found within the database
        homePage.show(username) 

    win.mainloop()
