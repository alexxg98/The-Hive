from tkinter import Label, Tk, Canvas, Frame, BOTH
from tkinter import * 
import datetime
import sys
import os
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1qaz@wsxEDC",
    database="TheHive",
    autocommit=True
)

cursor = db.cursor()

# Class to create the hexagon framework
class Hexagon(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Super User")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        #  Calculate dimensions: https://www.mathopenref.com/coordpolycalc.html
        # heaxagons
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
        canvas.create_text(150, 400, text = "Polls", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(150, 475, text = "Users", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(150, 550, text = "Groups", font = ("Pursia",15),
            fill = "white")

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
        canvas.create_text(850, 400, text = "Evaluate", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 475, text = "Complains", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 550, text = "Close", font = ("Pursia",15),
            fill = "white")
       
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

        # # Create a label with the name of the group
        # def write_group_name():
        #     #Get and store user info from database
        #     cursor.execute("SELECT name FROM users WHERE email = 'michael@gmail.com'")
        #     name = cursor.fetchone()[0]
        #     cursor.execute("SELECT reputation_score FROM users WHERE email = 'michael@gmail.com'")
        #     rep_score = cursor.fetchone()[0]
        #     cursor.close()
        #     canvas.create_text(120, 35, text = name, font = ("Pursia",25),fill = "#7289DB")
        
        time_now()
        # write_group_name
        canvas.pack(fill=BOTH, expand=1)
        canvas.configure(bg='#36393F')


        # Button for social
        # photo = PhotoImage(file = "user.png")
        # Button(canvas, text = 'Click Me !', image = photo).pack()


def main():
    root = Tk()
    frame = Hexagon()
    root.resizable(height = None, width = None)

    root.geometry("1000x800")  
    # Allowing root window to change 
    # it's size according to user's need 
    root.resizable(False, False) 
    root.mainloop()


if __name__ == '__main__':
    main() 