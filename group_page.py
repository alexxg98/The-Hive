from tkinter import*
import datetime
import sys
import os
import mysql.connector
import reputationScore as repScore
import db
import visitor
# import welcome

# Class to create the hexagon framework
class UI(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # UI settings
        canvas = Canvas(self)
        self.master.title("Super User")
        self.pack(fill=BOTH, expand=TRUE)
        canvas.pack(fill=BOTH, expand=1)
        canvas.configure(bg='#36393F')
        
        #Get and store user info from database
        group_name = db.getGroupName()
        group_rank = db.getGroupRank()
        group_description =db.getGroupDescription()
        rankDisplay = "Rank: " + str(group_rank)
        # db.cursor.close()  
        # Name of group
        canvas.create_text(100, 50, text = group_name, font = ("Pursia",25),
            fill = "#7289DB")
        # display group rank
        canvas.create_text(100, 100, text = rankDisplay, font = ("Pursia",15),
            fill = "#7289DB")
        # Display description
        canvas.create_text(100, 125, text = group_description, font = ("Pursia",15),
            fill = "#7289DB")

        #  Calculate dimensions: https://www.mathopenref.com/coordpolycalc.html
        # rectangleBox for the blog
        user_select_1 = [783,117,217,117,
                        217,117,217,683,
                        217,683,783,683,
                        783,683,783,117]

        canvas.create_polygon(user_select_1, outline='black',
            fill='#2C92D6', width=2)

        # Left Side Hexagon
        p1 = [97,388,75,375,
            75,375,53,388,
            53,388,53,413,
            53,413,75,425,
            75,425,97,413,
            97,413,97,388]
        p2 = [97,463,75,450,
            75,450,53,463,
            53,463,53,488,
            53,488,75,500,
            75,500,97,488,
            97,488,97,463]
        p3 = [97,538,75,525,
            75,525,53,538,
            53,538,53,563,
            53,563,75,575,
            75,575,97,563,
            97,563,97,538]

        canvas.create_polygon(p1,fill='#2C92D6', width=1)
        canvas.create_polygon(p2,fill='#37CAEF', width=1)
        canvas.create_polygon(p3,fill='#3EDAD8', width=1)
        # Left labels
        canvas.create_text(125, 400, text = "Polls", font = ("Pursia",15),
            fill = "white", anchor=W)
        canvas.create_text(125, 475, text = "Users", font = ("Pursia",15),
            fill = "white",anchor=W)
        canvas.create_text(125, 550, text = "Back", font = ("Pursia",15),
            fill = "white", anchor=W)

        # Right Side Hexagon
        g1 = [947,388,925,375,
            925,375,903,388,
            903,388,903,413,
            903,413,925,425,
            925,425,947,413,
            947,413,947,388]
        g2 = [947,463,925,450,
            925,450,903,463,
            903,463,903,488,
            903,488,925,500,
            925,500,947,488,
            947,488,947,463]
        g3 = [947,538,925,525,
            925,525,903,538,
            903,538,903,563,
            903,563,925,575,
            925,575,947,563,
            947,563,947,538]

        canvas.create_polygon(g1, fill='white', width=1)
        canvas.create_polygon(g2, fill='white', width=1)
        canvas.create_polygon(g3, fill='white', width=1)
        # group Labels
        canvas.create_text(875, 400, text = "Chat", font = ("Pursia",15),
            fill = "white", anchor=E)
        canvas.create_text(875, 475, text = "Schedule", font = ("Pursia",15),
            fill = "white", anchor=E)
        canvas.create_text(875, 550, text = "Post Docs", font = ("Pursia",15),
            fill = "white", anchor=E)
        
        # display date
        date = datetime.datetime.now()
        current_date = date.strftime("%B %d")
        canvas.create_text(900, 50, text = current_date, font = ("Pursia",20), fill = "white")
        canvas.create_text(900, 75, text = " ", fill = "white", tags='timer')

        def time_now():
            now = datetime.datetime.now()
            s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
            canvas.itemconfig('timer', text = s)
            self.after(100, time_now)
        time_now()
        
def main():
    root = Tk()
    frame = UI()

    posts = Text(root, height = 38, width = 70)
    posts.place(x = 250, y = 147)
    quote = """sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample.
    sample sample sample sample sample."""

    posts.insert(END, quote)

    # Button on left
    photo7 = PhotoImage(file = r"images/hexx.png")
    button = Button(root, image = photo7, bg='#2C92D6',  bd=0, command=polls).place(x=60, y=385)
    button = Button(root, image = photo7, bg="#37CAEF", bd=0, command=user_in_group).place(x=60, y=460)
    button = Button(root, image = photo7, bg="#3EDAD8", bd=0, command=lambda:back_bnt(root)).place(x=60, y=535)

    # Button on right
    photo6 = PhotoImage(file = r"images/hex.png")
    button = Button(root, image = photo6, bg="white", bd=0, command=chatwindow).place(x=909, y=385)
    button = Button(root, image = photo6, bg="white", bd=0, command=schedule).place(x=909, y=460)
    button = Button(root, image = photo6, bg="white", bd=0, command=postdoc).place(x=909, y=535)

    root.geometry("1000x800")
    root.resizable(False, False)
    root.mainloop()

def chatwindow():
    os.system('python3 chatwindow.py')
def postdoc():
    os.system('python3 postdoc.py')
def schedule():
    os.system('python3 schedule.py')
def user_in_group():
    os.system('python3 usersInGroup.py')
def polls():
    os.system('python3 polling.py')

def back_bnt(root):
    username =  db.getName()
    db.cursor.execute("SELECT user_type FROM users WHERE username = '%s'" % username)
    acct_type = db.cursor.fetchone()[0]
    if acct_type == "OU":
        ou(root)
    elif acct_type == "VIP":
        vip(root)
    elif acct_type == "SU":
        su(root)

def ou(root):
    root.destroy()
    os.system('python3 ou.py')

def vip(root):
    root.destroy()
    os.system('python3 vip.py')

def su(root):
    root.destroy()
    os.system('python3 su.py')


if __name__ == '__main__':
    main()
