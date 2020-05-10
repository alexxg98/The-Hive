# from tkinter import Label, Tk, Canvas, Frame, BOTH
from tkinter import *
import datetime
import sys
import os
import db

# Class to create the hexagon framework
class SU_GUI(Frame):

    def __init__(self):

        self.root = Tk()
        self.root.title("The Hive")
        self.root.geometry('{}x{}'.format(1000, 800))
        self.canvas = Canvas(self.root, bg='#36393F')
        self.initUI()
        self.buttons()
        
        # username on top label
        db.cursor.execute("SELECT username FROM users WHERE email = 'michael@gmail.com'")
        name = db.cursor.fetchone()[0]
        hello = "Hello " + name
        db.cursor.close()
        self.canvas.create_text(120, 35, text = hello, font = ("Pursia",25), fill = "#7289DB")

        def time_now():
            now = datetime.datetime.now()
            s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
            self.canvas.itemconfig('timer', text = s)
            self.after(100, self.time_now())

        # display date
        time_now()
        date = datetime.datetime.now()
        current_date = date.strftime("%B %d")
        self.canvas.create_text(500, 385, text = current_date, font = ("Pursia",20), fill = "black")
        self.canvas.create_text(500, 415, text = " ", fill = "black", tags='timer')


        

    # template UI with heaxagons
    def initUI(self):
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

        self.canvas.create_polygon(user_select_1, outline='black',
            fill='#2C92D6', width=2)
        self.canvas.create_polygon(user_select_2, outline='black',
            fill='#37CAEF', width=2)
        self.canvas.create_polygon(user_select_3, outline='black',
            fill='#3EDAD8', width=2)
        self.canvas.create_polygon(user_display_name, outline='black',
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

        self.canvas.create_polygon(s1, fill='white', width=1)
        self.canvas.create_polygon(s2, fill='white', width=1)
        self.canvas.create_polygon(s3, fill='white', width=1)

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

        self.canvas.create_polygon(p1,fill='#2C92D6', width=1)
        self.canvas.create_polygon(p2,fill='#37CAEF', width=1)
        self.canvas.create_polygon(p3,fill='#3EDAD8', width=1)
        # Left labels
        self.canvas.create_text(125, 400, text = "My Projects", font = ("Pursia",15),
            fill = "white", anchor=W)
        self.canvas.create_text(125, 475, text = "Users", font = ("Pursia",15),
            fill = "white",anchor=W)
        self.canvas.create_text(125, 550, text = "Groups", font = ("Pursia",15),
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

        self.canvas.create_polygon(g1, fill='white', width=1)
        self.canvas.create_polygon(g2, fill='white', width=1)
        self.canvas.create_polygon(g3, fill='white', width=1)
        # group Labels
        self.canvas.create_text(875, 400, text = "Evaluate", font = ("Pursia",15),
            fill = "white", anchor=E)
        self.canvas.create_text(875, 475, text = "Complains", font = ("Pursia",15),
            fill = "white", anchor=E)
        self.canvas.create_text(875, 550, text = "Other", font = ("Pursia",15),
            fill = "white", anchor=E)

    # get the current time - need to be modefied


    def buttons(self):
        # Main Hex buttons
        photo = PhotoImage(file = r"images/chat.png")
        left = Button(self.root, image = photo, bg="#2C92D6", bd=0, command=self.chatwindow).place(x=365, y=415)
        photo1 = PhotoImage(file = r"images/doc.png")
        right = Button(self.canvas, image = photo1, bg="#37CAEF", bd=0).place(x=570, y=415)
        photo2 = PhotoImage(file = r"images/social.png")
        top = Button(self.canvas, image = photo2, bg="#3EDAD8", bd=0, command=self.group_page).place(x=465, y=250)
        # Aux buttons
        photo3 = PhotoImage(file = r"images/add.png")
        add = Button(self.canvas, image = photo3, bg="white", bd=0).place(x=486, y=512)
        photo4 = PhotoImage(file = r"images/x.png")
        x = Button(self.canvas, image = photo4, bg="white", bd=0).place(x=375, y=325)
        photo5 = PhotoImage(file = r"images/settings.png")
        settings = Button(self.canvas, image = photo5, bg="white", bd=0).place(x=596, y=325)
        # Button on right
        photo6 = PhotoImage(file = r"images/hexx.png")
        button = Button(self.canvas, image = photo6, bg="white", bd=0, command=self.pendingUsers).place(x=909, y=385)
        button = Button(self.canvas, image = photo6, bg="white", bd=0).place(x=909, y=460)
        button = Button(self.canvas, image = photo6, bg="white", bd=0).place(x=909, y=535)
        # Button on left
        photo7 = PhotoImage(file = r"images/hex.png")
        button = Button(self.canvas, image = photo7, bg="#2C92D6", bd=0).place(x=60, y=385)
        button = Button(self.canvas, image = photo7, bg="#37CAEF", bd=0).place(x=60, y=460)
        button = Button(self.canvas, image = photo7, bg="#3EDAD8", bd=0).place(x=60, y=535)
        


    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.root.mainloop()

    def chatwindow(self):
        os.system('python chatwindow.py')

    def group_page(self):
        os.system('python group_page.py')

    def pendingUsers(self):
        os.system('python pendingUsers.py')

if __name__ == "__main__":
    x = SU_GUI()
    x.main()
