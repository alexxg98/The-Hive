import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cscD@t@Bas3",
    database="thehive"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM users")

result = cursor.fetchall()
for row in result: print(row)
