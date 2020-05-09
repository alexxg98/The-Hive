import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1qaz@wsxEDC",
    database="TheHive"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM users")

result = cursor.fetchall()
for row in result: print(row)
