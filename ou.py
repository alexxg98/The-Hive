from tkinter import Label, Tk, Canvas, Frame, BOTH
from tkinter import*
import datetime
import sys
import os
import mysql.connector

from reputationScore import *
import db

# Class to create the hexagon framework
class hexagon(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Ordinary User")
        self.pack(fill=BOTH, expand=TRUE)

        #Get and store user info from database
        db.cursor.execute("SELECT username FROM users WHERE status = 'ON'")
        name = db.cursor.fetchone()[0]
        db.cursor.execute("SELECT reputation_score FROM users WHERE status = 'ON'")
        rep_score = db.cursor.fetchone()[0]
        db.cursor.execute("SELECT taboo_count FROM users WHERE status = 'ON'")
        count = db.cursor.fetchone()[0]

        hello = "Hello " + name

        #Put into post file/part later
        # newScore = tabooWord(rep_score, count)
        # db.cursor.execute("UPDATE users SET reputation_score = '%d' WHERE status = 'ON'" %newScore)
        # count += 1
        # db.cursor.execute("UPDATE users SET taboo_count = '%d' WHERE status = 'ON'" %count)
        scoreDisplay = "Reputation Score: " + str(rep_score)
        db.cursor.close()


        canvas = Canvas(self)

        user_select_1 = [500,200,413,150,
                        413,150,326,200,
                        326,200,326,300,
                        326,300,413,350,
                        413,350,500,300,
                        500,300,500,200]
        user_select_2 = [675,200,588,150,
                        588,150,501,200,
                        501,200,501,300,
                        501,300,588,350,
                        588,350,675,300,
                        675,300,675,200]
        user_select_3 = [587,351,500,301,
                        500,301,413,351,
                        413,351,413,451,
                        413,451,500,501,
                        500,501,587,451,
                        587,451,587,351]
        user_display_name = [565,263,500,225,
                            500,225,435,263,
                            435,263,435,338,
                            435,338,500,375,
                            500,375,565,338,
                            565,338,565,263]
        canvas.create_polygon(user_select_1, outline='black', fill='#2C92D6', width=2)
        canvas.create_polygon(user_select_2, outline='black', fill='#37CAEF', width=2)
        canvas.create_polygon(user_select_3, outline='black', fill='#3EDAD8', width=2)
        canvas.create_polygon(user_display_name, outline='black', fill='#ffffff', width=2)

        # hexagon for projects
        p1 = [95,391,75,380,
              75,380,55,391,
              55,391,55,409,
              55,409,75,420,
              75,420,95,409,
              95,409,95,391]
        p2 = [95,466,75,455,
              75,455,55,466,
              55,466,55,484,
              55,484,75,495,
              75,495,95,484,
              95,484,95,466]
        p3 = [95,541,75,530,
              75,530,55,541,
              55,541,55,559,
              55,559,75,570,
              75,570,95,559,
              95,559,95,541]
        canvas.create_polygon(p1,fill='#2C92D6', width=1)
        canvas.create_polygon(p2,fill='#37CAEF', width=1)
        canvas.create_polygon(p3,fill='#3EDAD8', width=1)

        # hexagon for user select
        s1 = [520,167,500,156,
              500,156,480,167,
              480,167,480,185,
              480,185,500,196,
              500,196,520,185,
              520,185,520,167]
        s2 = [412,354,392,343,
              392,343,372,354,
              372,354,372,372,
              372,372,392,383,
              392,383,412,372,
              412,372,412,354]
        s3 = [629,354,609,343,
              609,343,589,354,
              589,354,589,372,
              589,372,609,383,
              609,383,629,372,
              629,372,629,354]
        canvas.create_polygon(s1, fill='white', width=1)
        canvas.create_polygon(s2, fill='white', width=1)
        canvas.create_polygon(s3, fill='white', width=1)

        canvas.create_text(150, 400, text = "Project 1", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(150, 475, text = "Project 2", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(150, 550, text = "Project 3", font = ("Pursia",15),
            fill = "white")
        # hexagon for groups
        g1 = [795,391,775,380,
              775,380,755,391,
              755,391,755,409,
              755,409,775,420,
              775,420,795,409,
              795,409,795,391]
        g2 = [795,466,775,455,
              775,455,755,466,
              755,466,755,484,
              755,484,775,495,
              775,495,795,484,
              795,484,795,466]
        g3 = [795,541,775,530,
              775,530,755,541,
              755,541,755,559,
              755,559,775,570,
              775,570,795,559,
              795,559,795,541]
        canvas.create_polygon(g1, fill='white', width=1)
        canvas.create_polygon(g2, fill='white', width=1)
        canvas.create_polygon(g3, fill='white', width=1)
        canvas.create_text(850, 400, text = "Group 1", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 475, text = "Group 2", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 550, text = "Group 3", font = ("Pursia",15),
            fill = "white")

        canvas.pack(fill=BOTH, expand=1)
        canvas.configure(bg='#36393F')
        # display date
        date = datetime.datetime.now()
        current_date = date.strftime("%B %d")
        canvas.create_text(500, 300, text = current_date, font = ("Pursia",20), fill = "black")
        canvas.create_text(500, 330, text = " ", fill = "black", tags='timer')

        def time_now():
            now = datetime.datetime.now()
            s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
            canvas.itemconfig('timer', text = s)
            self.after(100, time_now)
        time_now()

        # greeting for user
        canvas.create_text(120, 50, text = hello, font = ("Pursia",25),
            fill = "#7289DB")
        # display user score
        canvas.create_text(120, 100, text = scoreDisplay, font = ("Pursia",15),
            fill = "#7289DB")
        # My Projects
        canvas.create_text(120, 340, text = "MY PROJECTS", font = ("Pursia",15),
            fill = "#7289DB")
        canvas.create_text(815, 340, text = "MY GROUPS", font = ("Pursia",15),
            fill = "#7289DB")



def main():
    root = Tk()
    frame = hexagon()
    # Buttons
    photo1 = PhotoImage(file = r"images\chat.png")
    button1 = Button(root, image = photo1, bg="#2C92D6", bd=0, command=chatwindow).place(x=365, y=220)
    photo2 = PhotoImage(file = r"images\doc.png")
    button2 = Button(root, image = photo2, bg="#37CAEF", bd=0).place(x=567, y=230)
    photo3 = PhotoImage(file = r"images\social.png")
    button3 = Button(root, image = photo3, bg="#3EDAD8", bd=0).place(x=465, y=390)
    photo4 = PhotoImage(file = r"images\add.png")
    button4 = Button(root, image = photo4, bg="white", bd=0).place(x=487, y=164)
    photo5 = PhotoImage(file = r"images\x.png")
    button5 = Button(root, image = photo5, bg="white", bd=0).place(x=379, y=350)
    photo6 = PhotoImage(file = r"images\settings.png")
    button6 = Button(root, image = photo6, bg="white", bd=0).place(x=596, y=351)

    root.geometry("1000x800")
    root.resizable(False, False)
    root.mainloop()

def chatwindow():
    os.system('python chatwindow.py')


if __name__ == '__main__':
    main()
