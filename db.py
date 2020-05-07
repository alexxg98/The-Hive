import mysql.connector

# change details here only once
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="TheHive",
    autocommit=True
)

cursor = db.cursor()
