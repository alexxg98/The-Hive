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


def generate_username(name):
    letters = name[0] + " ".join(name.split()[1:2])
    number = random.randint(100, 999)
    username = letters + str(number)
    return username.lower()


class SuperUser:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(1000, 450))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.acceptButton = Button(self.canvas, text="Accept", font='Arial 15 bold', bg='#454b54',
                                   fg="#f7cc35", command=self.accept)
        self.rejectButton = Button(self.canvas, text="Reject", font='Arial 15 bold', bg='#454b54',
                                   fg="#f7cc35", command=self.reject)
        self.list = Treeview(self.canvas, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="15")

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)

        self.list.pack()
        self.list.heading(1, text="ID")
        self.list.column(1, width=20)
        self.list.heading(2, text="Name")
        self.list.column(2, width=100)
        self.list.heading(3, text="Email")
        self.list.column(3, width=150)
        self.list.heading(4, text="Reference")
        self.list.column(4, width=100)
        self.list.heading(5, text="Interest")
        self.list.column(5, width=100)
        self.list.heading(6, text="Credential")
        self.list.column(6, width=100)
        self.list.heading(7, text="Rejected #")
        self.list.column(7, width=120)
        self.list.heading(8, text="Appeal")
        self.list.column(8, width=300)

        db.cursor.execute('SELECT * FROM pending_users')
        for row in db.cursor.fetchall():
            self.list.insert('', END, values=row)

        self.acceptButton.pack(expand=TRUE, side=LEFT)
        self.rejectButton.pack(expand=TRUE, side=LEFT)

        self.win.mainloop()

    def accept(self):
        password = ''.join(random.choice(string.ascii_lowercase) for i in range(6))

        for selected_item in self.list.selection():
            a, b, c, d, e, f, g, h = self.list.item(selected_item, 'values')
            email = c
            username = generate_username(b)
            self.list.delete(selected_item)

        db.cursor.execute('INSERT INTO users (email, username, password, user_type, login_time) VALUES (%s, %s, %s, "OU", "FIRST")',
                          (email, username, password))
        db.cursor.execute("DELETE FROM pending_users WHERE email = %s", (email,))

        subject = "Application Accepted!"
        content = '''\
            Congratz! Please change your password once you log in with the following credentials. \n
            Username: {username} \n
            Password: {password} \
            '''.format(username=username, password=password)
        send_email(subject, content, email)

    def reject(self):
        for selected_item in self.list.selection():
            email = self.list.item(selected_item, 'values')[2]
            self.list.delete(selected_item)

        db.cursor.execute("SELECT rejected FROM pending_users WHERE email = %s", (email,))
        rejNum = db.cursor.fetchone()[0]

        if rejNum == 0:
            rejNum += 1
            db.cursor.execute("UPDATE pending_users SET rejected = %s WHERE email = %s", (rejNum,email))

            subject = "Application Denied"
            content = '''\
                Sorry, but your application has been denied. \n
                You have one chance to appeal and the SU will make a final decision to \n
                reverse the rejection. If you receive another rejection, then you \n
                will be put in blacklist forever.  \
                '''
            send_email(subject, content, email)
        elif rejNum == 1:
            db.cursor.execute("DELETE FROM pending_users WHERE email = %s", (email,))
            db.cursor.execute("INSERT INTO black_list VALUES (%s, %s)", (db.getName(), email))


if __name__ == "__main__":
    x = SuperUser()
    x.main()
