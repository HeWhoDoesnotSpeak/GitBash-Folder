import sqlite3
import os

os.system('clear')
connection = sqlite3.connect("login_details.db")
cursor = connection.cursor()


#Create at table named login


