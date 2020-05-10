from tkinter import Label, Tk, Canvas, Frame, BOTH
from tkinter import *
import datetime
import sys
import os
import mysql.connector
import db

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
        user_select_1 = [674,401,587,351,
                    587,351,500,401,
                    500,401,500,501,
                    500,501,587,551,
                    587,551,674,501,
                    674,501,674,401]
        user_select_2 = [499,401,412,351,
                    412,351,325,401,
                    325,401,325,501,
                    325,501,412,551,
                    412,551,499,501,
                    499,501,499,401]
        user_select_3 = [587,250,500,200,
                    500,200,413,250,
                    413,250,413,350,
                    413,350,500,400,
                    500,400,587,350,
                    587,350,587,250]
        user_display_name = [552,370,500,340,
                    500,340,448,370,
                    448,370,448,430,
                    448,430,500,460,
                    500,460,552,430,
                    552,430,552,370]

        canvas.create_polygon(user_select_1, outline='black',
            fill='#2C92D6', width=2)
        canvas.create_polygon(user_select_2, outline='black',
            fill='#37CAEF', width=2)
        canvas.create_polygon(user_select_3, outline='black',
            fill='#3EDAD8', width=2)
        canvas.create_polygon(user_display_name, outline='black',
            fill='#ffffff', width=2)

        # hexagon for user select
        s1 = [412,325,390,312,
            390,312,368,325,
            368,325,368,350,
            368,350,390,362,
            390,362,412,350,
            412,350,412,325]
        s2 = [632,325,610,312,
            610,312,588,325,
            588,325,588,350,
            588,350,610,362,
            610,362,632,350,
            632,350,632,325]
        s3 = [522,515,500,502,
            500,502,478,515,
            478,515,478,540,
            478,540,500,552,
            500,552,522,540,
            522,540,522,515]

        canvas.create_polygon(s1, fill='white', width=1)
        canvas.create_polygon(s2, fill='white', width=1)
        canvas.create_polygon(s3, fill='white', width=1)

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
        canvas.create_text(150, 400, text = "My Projects", font = ("Pursia",15),
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
        canvas.create_text(850, 550, text = "Other", font = ("Pursia",15),
            fill = "white")

        # display date
        date = datetime.datetime.now()
        current_date = date.strftime("%B %d")
        canvas.create_text(500, 385, text = current_date, font = ("Pursia",20), fill = "black")
        canvas.create_text(500, 415, text = " ", fill = "black", tags='timer')

        def time_now():
            now = datetime.datetime.now()
            s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
            canvas.itemconfig('timer', text = s)
            self.after(100, time_now)

        # Create a label with the name of the user
        def write_welcome():
            #Get and store user info from database
            name = db.getName()
            rep_score = db.getRepScore()

            hello = "Hello " + name
            canvas.create_text(120, 35, text = hello, font = ("Pursia",25),
                    fill = "#7289DB")

        time_now()
        write_welcome()
        canvas.pack(fill=BOTH, expand=1)
        canvas.configure(bg='#36393F')


        # Button for social
        # photo = PhotoImage(file = "user.png")
        # Button(canvas, text = 'Click Me !', image = photo).pack()


def main():
    root = Tk()

    # creates heaxagon main screen 
    frame = Hexagon()

    # Button on main Hex
    photo4 = PhotoImage(file = r"images/add.png")
    button4 = Button(root, image = photo4, bg="white", bd=0).place(x=486, y=512)
    photo2 = PhotoImage(file = r"images/doc.png")
    button2 = Button(root, image = photo2, bg="#37CAEF", bd=0).place(x=570, y=415)
    photo3 = PhotoImage(file = r"images/social.png")
    button3 = Button(root, image = photo3, bg="#3EDAD8", bd=0).place(x=465, y=250)
    photo5 = PhotoImage(file = r"images/x.png")
    button5 = Button(root, image = photo5, bg="white", bd=0).place(x=375, y=325)
    photo6 = PhotoImage(file = r"images/settings.png")
    button6 = Button(root, image = photo6, bg="white", bd=0).place(x=596, y=325)
    # Button on right
    photo7 = PhotoImage(file = r"images/hexx.png")
    button = Button(root, image = photo7, bg="white", bd=0).place(x=909, y=385)
    button = Button(root, image = photo7, bg="white", bd=0).place(x=909, y=460)
    button = Button(root, image = photo7, bg="white", bd=0).place(x=909, y=535)
    # Button on left
    photo7 = PhotoImage(file = r"images/hex.png")
    button = Button(root, image = photo7, bg="#2C92D6", bd=0).place(x=60, y=385)
    button = Button(root, image = photo7, bg="#37CAEF", bd=0).place(x=60, y=460)
    button = Button(root, image = photo7, bg="#3EDAD8", bd=0).place(x=60, y=535)
    
    root.resizable(height = None, width = None)
    root.geometry("1000x800")  
    root.resizable(False, False) 
    root.mainloop()


if __name__ == '__main__':
    main()
