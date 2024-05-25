from tkinter import *
import subprocess
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os


os.system('clear')
connection = sqlite3.connect("login_details.db")
cursor = connection.cursor()

def dbLogin():
    create = """CREATE TABLE IF NOT EXISTS login_details (UserName text, Password text,  Email text)"""
    cursor.execute(create)
    print("Login Details \n")
    cursor.execute("SELECT * FROM login_details")
    connection.commit()
    results = cursor.fetchall()
    print(results)
    print("")
    cursor.execute("SELECT Password FROM login_details")
    connection.commit()
    results = cursor.fetchall()
    print(results)
    
dbLogin()

def register():
    messagebox.showinfo("","Thank you for registering")
    win.destroy()
    subprocess.run(["python", "GitBash Folder//FrontPage.py"])
    
     
win = Tk()
win.title("Register")
win.geometry("300x200")
       
Label(win, text="UserName").place(x=10, y=10)
Label(win, text="Password").place(x=10, y=40)
un =Entry()
pw =Entry()

def text():
      un = Entry(win)
      un.place(x=140, y=10)
      pw = Entry(win)
      pw.place(x=140, y=40)

text()


entry=("UPDATE login_details SET UserName = %s, SET PASSWORD = %s WHERE id=%s") 
val= (un,pw,id)

cursor.execute(entry,val)

Button(win, text="Register", command=register, height=3, width=20).place(x=10,y=120)  
cursor.close()
win.mainloop()