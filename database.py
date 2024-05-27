import sqlite3

#Calls the connection to be made the two
def getConnection():
    connection = sqlite3.connect("GitBash Folder//loginDetails.db")
    return connection

#Creates the table if not already existing
def createTable():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS loginDetails (UserName text, Password text, Email text)""")
    connection.commit()
    connection.close()

# Inserts user's details into the database to be saved
def insertUser(username, password, email):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO loginDetails (UserName, Password, Email) VALUES (?, ?, ?)", (username, password, email))
    connection.commit()
    connection.close()

# Collects the user's username
def getUser(username):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM loginDetails WHERE UserName=?", (username,))
    user = cursor.fetchone()
    connection.close()
    return user
