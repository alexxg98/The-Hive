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
    return cursor.fetchone()[0]


def getRepScore():
    cursor.execute("SELECT reputation_score FROM users WHERE status = 'ON'")
    return cursor.fetchone()[0]


def getTabooCount():
    cursor.execute("SELECT taboo_count FROM users WHERE status = 'ON'")
    return cursor.fetchone()[0]


def getGroupName():
    username = getName()
    cursor.execute("SELECT name from projects A\
            INNER JOIN group_membership B\
            on A.id = B.group_id where B.username = %s", (username,))
    return cursor.fetchone()[0]

def getGroupRank():
    groupID = getGroupID()
    cursor.execute("SELECT projRank FROM projects WHERE id = %s",(groupID,))
    return cursor.fetchone()[0]

def getGroupDescription():
    groupID = getGroupID()
    cursor.execute("SELECT description FROM projects WHERE id = %s",(groupID,))
    return cursor.fetchone()[0]

def getGroupID():
    username = getName()
    cursor.execute("SELECT id from projects A\
                INNER JOIN group_membership B\
                on A.id = B.group_id where B.username = %s", (username,))
    return cursor.fetchone()[0]
    
def getPostCount():
    groupId = getGroupID()
    cursor.execute("SELECT postid FROM posts WHERE group_id = '%d' ORDER BY postid DESC LIMIT 1" % groupId)
    return cursor.fetchone()[0]
