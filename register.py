from tkinter import *
from tkinter import messagebox
import smtplib

import welcome
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="alfheim",
    database="TheHive"
)

cursor = db.cursor()


def send_email(receiver):
    sender = "thehiveof4men@gmail.com"
    password = "thehive111"
    message = "Hey, this was sent from Super User"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    server.quit()


class RegisterWindow:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.nameLabel = Label(self.canvas, text="Name", font='Arial 15 bold', bg='#454b54',
                               fg='#f7cc35')
        self.name = Entry(self.canvas, font='Arial 15 bold', bg='white')

        self.emailLabel = Label(self.canvas, text="Email", font='Arial 15 bold', bg='#454b54',
                                fg='#f7cc35')
        self.email = Entry(self.canvas, font='Arial 15 bold', bg='white')

        self.refLabel = Label(self.canvas, text="Reference", font='Arial 15 bold', bg='#454b54',
                              fg='#f7cc35')
        self.reference = Entry(self.canvas, font='Arial 15 bold', bg='white')

        self.interestLabel = Label(self.canvas, text="Interest", font='Arial 15 bold', bg='#454b54',
                                   fg='#f7cc35')
        self.interest = Entry(self.canvas, font='Arial 15 bold', bg='white')

        self.credLabel = Label(self.canvas, text="Credential", font='Arial 15 bold', bg='#454b54',
                               fg='#f7cc35')
        self.credential = Entry(self.canvas, font='Arial 15 bold', bg='white')

        self.backButton = Button(self.canvas, text="Back", font='Arial 15 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.welcome)
        self.regButton = Button(self.canvas, text="Register", font='Arial 15 bold', bg='#454b54', fg='#f7cc35',
                                command=lambda: self.reg_btn())

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)

        self.nameLabel.pack(expand=TRUE)
        self.name.pack(expand=TRUE)

        self.emailLabel.pack(expand=TRUE)
        self.email.pack(expand=TRUE)

        self.refLabel.pack(expand=TRUE)
        self.reference.pack(expand=TRUE)

        self.interestLabel.pack(expand=TRUE)
        self.interest.pack(expand=TRUE)

        self.credLabel.pack(expand=TRUE)
        self.credential.pack(expand=TRUE)

        self.backButton.pack(expand=TRUE)
        self.regButton.pack(expand=TRUE)

        self.win.mainloop()

    def reg_btn(self):
        name = self.name.get()
        email = self.email.get()
        reference = self.reference.get()
        interest = self.interest.get()
        credential = self.credential.get()

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        account = cursor.fetchone()

        if name == "" or email == "" or reference == "" or interest == "" or credential == "":
            messagebox.showwarning("Registration Status", "All fields are required!")
        elif not account:
            messagebox.showinfo("Registration Status", "Thank You! A SuperUser will review your application "
                                                       "and if approved, an email will be sent to you with "
                                                       "your login details.")
            send_email(email)
        else:
            messagebox.showerror("Registration Status", "Account with this email already exists!")

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()
