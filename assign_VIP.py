import string
import random
from tkinter import *
import smtplib
from email.message import EmailMessage
from tkinter.ttk import Treeview
import db


def send_email(subject, content, receiver):
    sender = "thehiveof4men@gmail.com"
    password = "thehive111"

    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    message.set_content(content)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()

class Assing_VIP_UI:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        # self.canvas = Canvas(self.win, bg='#454b54')
        
        self.canvas = Canvas(self.win, bg='#454b54')
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame = Frame(self.canvas, bg='#454b54', width=600, height=340)
        self.frame.pack(expand=TRUE)
        self.tree = Treeview(self.frame, columns=2, show="headings", height="7")
        self.list = Treeview(self.frame, columns=(1, 2, 3, 4, 5), show="headings", height="15")

    def main(self):
        Label(self.frame, text="Groups:", bg="#454b54", fg="#f7cc35",
        font="Arial 14 bold").grid(row=0, column=0)
        Label(self.frame, text="VIP Users:", bg="#454b54", fg="#f7cc35",
        font="Arial 14 bold").grid(row=0, column=1)

        self.list.grid(row = 1, column = 0, sticky = N, pady = 2)
        self.list.heading(1, text="ID")
        self.list.column(1, width=20)
        self.list.heading(2, text="Name")
        self.list.column(2, width=100)
        self.list.heading(3, text="Description")
        self.list.column(3, width=200)
        self.list.heading(4, text="Creator")
        self.list.column(4, width=100)
        self.list.heading(5, text="Rank")
        self.list.column(5, width=100)

        self.tree.grid(row = 1, column = 1, sticky = N, pady = 2)
        self.tree.heading(2, text="Select User")

        db.cursor.execute('SELECT * FROM projects;')
        records = db.cursor.fetchall()
        for row in records:
            self.list.insert('', END, values=row)

        db.cursor.execute('SELECT username FROM users WHERE user_type="VIP"')
        users = db.cursor.fetchall()
        for row in users:
            self.tree.insert('', END, values=row)

        
        Button(self.frame, text="Select Group",font='Arial 15 bold', bg='#454b54',
            fg="#f7cc35", command=self.select).grid(row=2, column=0, sticky = N, pady = 2)
        Button(self.frame, text="Select VIP user", font='Arial 15 bold', bg='#454b54',
            fg="#f7cc35", command=self.select).grid(row=2, column=1, sticky = N, pady = 2)
        Button(self.frame, text="ASSIGN",font='Arial 15 bold', bg='black',
            fg="red", command=self.assign).grid(row=3, column=1, pady = 2)

        # group_name =
        # user_name = 
        selected_label = "Selected User: " 
        Label(self.frame, text=selected_label, bg="#454b54", fg="white",
        font="Arial 14 bold").grid(row=3, column=0, sticky = SW, pady = 25)

        self.win.mainloop()

    def assign(self):
        for selected_item in self.list.selection():
            a, b, c, d, e, f = self.list.item(selected_item, 'values')
            email = c

        for selected_item in self.list.selection():
            self.list.delete(selected_item)

        subject = "Group Assigned for Evaluation"
        content = '''\
            Dear VIP User, 
            I've Assigned you this group for evaluation, as they had requested 
            to close the group.  \
            '''
        send_email(subject, content, email)

    def select(self):
        select 


if __name__ == "__main__":
    x = Assing_VIP_UI()
    x.main()

