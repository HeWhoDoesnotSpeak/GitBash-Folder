import sqlite3
from tkinter import messagebox

# Establishes a connection to the SQLite database
def getConnection():
    try:
        return sqlite3.connect("C://Users//64223/CPS//GitBash Folder//mainDB.db")
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

# Checks if the database connection was successful and handles error messaging
def checkConnection(printFunction, messageFunction, printText, messageText):
    connection = getConnection()
    if connection is None:
        printFunction(printText)
        messageFunction(messageText)
        return None
    return connection

# Creates the necessary tables if they don't already exist
def createTables():
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        # Creates users, articles, and history tables if they don't already exist
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
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return
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

# Retrieves a specific user by their username
def getUser(username):
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return None
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE UserName=?", (username,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving the user: {e}")
    finally:
        connection.close()

# Retrieves all users that are currently in the database
def getAllUsers():
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT UserName FROM users")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving users: {e}")
    finally:
        connection.close()

# Checks if a user exists by using the username within the database
def checkUserExists(username):
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
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
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return
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

# Retrieves all articles from the database to be displayed later
def getAllArticles():
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT title, content FROM articles")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving articles: {e}")
    finally:
        connection.close()

# Updates an existing article with new content that already exists in the database
def updateArticle(title, newContent):
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE articles SET content=? WHERE title=?", (newContent, title))
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while updating the article: {e}")
    finally:
        connection.close()

# Saves the search history entry for a user from the database that is currently logged in
def saveSearchHistory(username, question):
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO history (UserName, question) VALUES (?, ?)", (username, question))
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while trying to save the search history: {e}")
    finally:
        connection.close()

# Retrieves the search history for a specific user that is chosen by the username in the database
def getSearchHistory(username):
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM history WHERE UserName=? ORDER BY number DESC", (username,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving the search history: {e}")
        return []
    finally:
        connection.close()

# Updates the password for a specific user
def updateUserPassword(username, newPassword):
    connection = checkConnection(print, messagebox.showerror, "Failed to connect to database", "Failed to connect to the database")
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET Password=? WHERE UserName=?", (newPassword, username))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"No user found with username '{username}'")
    except sqlite3.Error as e:
        print(f"An error occurred while updating the password: {e}")
    finally:
        connection.close()
