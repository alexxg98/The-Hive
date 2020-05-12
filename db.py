import mysql.connector

# change details here only once
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1qaz@wsxEDC",
    database="TheHive",
    autocommit=True
)

cursor = db.cursor()

def getName():
    cursor.execute("SELECT username FROM users WHERE status = 'ON'")
    return (cursor.fetchone()[0])

def getRepScore():
    cursor.execute("SELECT reputation_score FROM users WHERE status = 'ON'")
    return (cursor.fetchone()[0])

def getTabooCount():
    cursor.execute("SELECT taboo_count FROM users WHERE status = 'ON'")
    return (cursor.fetchone()[0])

def getGroupName():
    username = 'michael002';
    cursor.execute("SELECT name FROM projects WHERE username = '%s'",(username,))
    return (cursor.fetchone()[0])

def getGroupRank():
    groupName = getGroupName
    cursor.execute("SELECT projRank FROM projects WHERE username = '%s'",(groupName,))
    return (cursor.fetchone()[0])

