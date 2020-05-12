import string
import random
from tkinter import *
import smtplib
from email.message import EmailMessage
from tkinter.ttk import Treeview
import db

class SuperUser:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(700, 400))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.widget = Label(self.canvas, text='Select User to kick out: ', font='Arial 15 bold',fg='white', bg='#454b54')
        self.close_btn = Button(self.canvas, text="Close", font='Arial 15 bold', bg='#454b54',
                                   fg="#f7cc35", command=quit)
        self.list = Treeview(self.canvas, columns=(1, 2, 3, 4, 5), show="headings", height="15")

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.widget.pack(fill=X)
        self.list.pack()
        self.list.heading(1, text="Username")
        self.list.column(1, width=100)
        self.list.heading(2, text="Email")
        self.list.column(2, width=200)
        self.list.heading(3, text="Reputation")
        self.list.column(3, width=65)
        self.list.heading(4, text="Type")
        self.list.column(4, width=50)

        db.cursor.execute('SELECT * FROM group_membership')
        for row in db.cursor.fetchall():
            self.list.insert('', END, values=row)

        self.close_btn.pack(expand=TRUE)        
        self.win.mainloop()


if __name__ == "__main__":
    x = SuperUser()
    x.main()

