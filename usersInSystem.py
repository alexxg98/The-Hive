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

class SuperUser:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(700, 400))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.widget = Label(self.canvas, text='Select User to kick out: ', font='Arial 15 bold',fg='white', bg='#454b54')
        self.kickOutbutton = Button(self.canvas, text="Kick Out User", font='Arial 15 bold', bg='#454b54',
                                   fg="#f7cc35", command=self.kickOut)
        # self.close_group = Button(self.canvas, text="Close Group", font='Arial 15 bold', bg='#454b54',
        #                            fg="#f7cc35", command=self.closeGropu)
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
        self.list.heading(5, text="Taboo")
        self.list.column(5, width=50)

        db.cursor.execute(' SELECT username,email,reputation_score,user_type,taboo_count FROM users;')
        for row in db.cursor.fetchall():
            self.list.insert('', END, values=row)

        self.kickOutbutton.pack(expand=TRUE)
        # self.close_group.pack(expand=TRUE, side=LEFT)
        
        self.win.mainloop()

    def kickOut(self):
        for selected_item in self.list.selection():
            username = self.list.item(selected_item, 'values')[0]
            email = self.list.item(selected_item, 'values')[1]
            self.list.delete(selected_item)

        db.cursor.execute("DELETE FROM users WHERE username = %s", (username,))

        subject = "REMOVED from 'The Hive'"
        content = '''\
            Dear {username}, \n
            You have been REMOVED from out system 'The Hive' for breaking our policies.\n
            If you believe we've aken a mistake please reach out to a Super User.\n\n
            Best Regards,\n
            The Hive Team
            '''.format(username=username)
        send_email(subject, content, email)


    def closeGropu(self):
        for selected_item in self.list.selection():
            a, b, c, d, e, f = self.list.item(selected_item, 'values')
            group_name = c
            self.list.delete(selected_item)
        db.cursor.execute("DELETE FROM pending_users WHERE email = %s", (group_name,))


if __name__ == "__main__":
    x = SuperUser()
    x.main()

