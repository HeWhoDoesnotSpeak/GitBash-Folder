from tkinter import *
import subprocess
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os

os.system('clear')
connection = sqlite3.connect("login_details.db")
cursor = connection.cursor()

def login(username, password):
      
      cursor.execute('select %s from db') % username
      dbuser = cursor.fetchone()
      if dbuser == username:
        cursor.execute('select %s from db') % password
        dbpass = cursor.fetchone()
        if dbpass == password:
            return "True"
        else:
            return "Password is incorrect."
      else:
       return "Username is incorrect."
      if(UserName == "" and Password == "") :
           messagebox.showinfo("", "Blank Not allowed")
      elif(UserName == login_details(UserName) and Password == login_details(Password)):        
           messagebox.showinfo("","Login Success")
           win.destroy()
           subprocess.run(["python", "GitBash Folder//HomePage.py"])
      else:
           messagebox.showinfo("","Incorrent Username and Password")
      
      

def register():
    messagebox.showinfo("","Please Register")
    win.destroy()
    subprocess.run(["python", "GitBash Folder//Register.py"])


win = Tk()
win.title("Login")
win.geometry("300x200")
       
Label(win, text="UserName").place(x=10, y=10)
Label(win, text="Password").place(x=10, y=40)
       
def text():
      e1 = Entry(win)
      e1.place(x=140, y=10)
      e2 = Entry(win)
      e2.place(x=140, y=40)
      e2.config(show="*")

text()

Button(win, text="Login", command=login ,height = 3, width = 20).place(x=10, y=80)
Button(win, text="Register", command=register, height=3, width=20).place(x=10,y=120) 


win.mainloop()