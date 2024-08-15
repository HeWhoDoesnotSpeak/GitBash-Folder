import sqlite3
from tkinter import messagebox

# Establishes a connection to the SQLite database
def getConnection():
    try:
        return sqlite3.connect("C://Users//64223/CPS//GitBash Folder//mainDB.db")
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

def checkConnection(printFunction, messageFunction, printText, messageText):
    connection = getConnection()
    if connection is None:
        printFunction(printText)
        messageFunction(messageText)
        return

# Creates the necessary tables if they don't already exist
def createTables():
    connection = getConnection()
    checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (UserName TEXT PRIMARY KEY, Password TEXT, Email TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS articles (title TEXT PRIMARY KEY, content TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS history (number INTEGER PRIMARY KEY AUTOINCREMENT, UserName TEXT, question TEXT, FOREIGN KEY(UserName) REFERENCES users(UserName))")
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while creating tables: {e}")
        messagebox.showerror("Error", "An error occurred while creating tables.")
    finally:
        connection.close()

# Inserts a new user into the database
def insertUser(username, password, email):
    connection = getConnection()
    checkConnection(print, messagebox.showerror, "Failed to connect to database","Failed to connect to the database")
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (UserName, Password, Email) VALUES (?, ?, ?)", (username, password, email))
        connection.commit()
    except sqlite3.IntegrityError:
        print(f"User with username '{username}' already exists.")
    except sqlite3.Error as e:
        print(f"An error occurred while inserting the user: {e}")
    finally:
        connection.close()

# Retrieves a user by their username
def getUser(username):
    connection = getConnection()
    checkConnection(print, messagebox.showerror, "Failed to connect to database","Failed to connect to the database")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE UserName=?", (username,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving the user: {e}")
    finally:
        connection.close()

# Retrieves all users from the database
def getAllUsers():
    connection = getConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT UserName FROM users")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving users: {e}")
    finally:
        connection.close()

# Checks if a user exists by username by search the database with all usernames
def checkUserExists(username):
    connection = getConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT UserName FROM users WHERE UserName=?", (username,))
        return cursor.fetchone() is not None
    except sqlite3.Error as e:
        print(f"An error occurred while checking if the user exists: {e}")
    finally:
        connection.close()

# Inserts an article into the database
def saveArticle(title, content):
    connection = getConnection()
    checkConnection(print, messagebox.showerror, "Failed to connect to database","Failed to connect to the database")
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO articles (title, content) VALUES (?, ?)", (title, content))
        connection.commit()
    except sqlite3.IntegrityError:
        print(f"Article with title '{title}' already exists.")
    except sqlite3.Error as e:
        print(f"An error occurred while saving the article: {e}")
    finally:
        connection.close()

# Retrieves all articles from the database
def getAllArticles():
    connection = getConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT title, content FROM articles")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving articles: {e}")
    finally:
        connection.close()

def updateArticle(title, newContent):
    connection = getConnection()
    checkConnection(print, messagebox.showerror, "Failed to connect to databse","Failed to connect to the database")
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE articles SET content=? WHERE title=?", (newContent, title))
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while updating the article: {e}")
    finally:
        connection.close()

def saveSearchHistory(username, question):
    connection = getConnection()
    checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    try:
        cursor = connection.cursor()
        # Adjust column name to match the existing schema
        cursor.execute("INSERT INTO history (username, question) VALUES (?, ?)", (username, question))
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while trying to save the search history: {e}")
    finally:
        connection.close()

def getSearchHistory(username):
    connection = getConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return []
    try:
        cursor = connection.cursor()
        # Adjust column name to match the existing schema
        cursor.execute("SELECT * FROM history WHERE username=? ORDER BY number DESC", (username,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving the search history: {e}")
        return []
    finally:
        connection.close()




