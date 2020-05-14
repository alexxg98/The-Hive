from tkinter import *
from tkinter import messagebox
import db
import login


class ChangePassword:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.title = Label(self.canvas, text="Change Password", font='Arial 15 bold', bg='#454b54',
                                fg='#f7cc35')

        self.emailLabel = Label(self.canvas, text="Email", font='Arial 15 bold', bg='#454b54',
                                fg='#f7cc35')
        self.email = Entry(self.canvas, font='Arial 15 bold', bg='white')

        self.newPassLabel = Label(self.canvas, text="Enter New Password", font='Arial 15 bold', bg='#454b54',
                               fg='#f7cc35')
        self.newPass = Entry(self.canvas, font='Arial 15 bold', bg='white')


        self.submit = Button(self.canvas, text="Submit", font='Arial 15 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.submit_btn)

        self.backButton = Button(self.canvas, text="Back", font='Arial 15 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.login)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.title.pack(expand=TRUE)
        self.emailLabel.pack(expand=TRUE)
        self.email.pack(expand=TRUE)
        self.newPassLabel.pack(expand=TRUE)
        self.newPass.pack(expand=TRUE)
        self.submit.pack(expand=TRUE)
        self.backButton.pack(expand=TRUE)
        self.win.mainloop()

    def submit_btn(self):
        email = self.email.get()
        newPass = self.newPass.get()

        db.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        registered = db.cursor.fetchone()

        #Check if first time login
        db.cursor.execute("SELECT login_time FROM users WHERE email = '%s'" % email)
        firstLogin = db.cursor.fetchone()[0]

        if registered:
            messagebox.showinfo("Password Change", "Your password has been updated.")
            db.cursor.execute('UPDATE users SET password = %s WHERE email = %s', (newPass, email))

            #Not first time login anymore
            if firstLogin == "FIRST":
                db.cursor.execute('UPDATE users SET login_time = NULL WHERE email = %s', (email,))
            self.login()

        else:
            messagebox.showinfo("Password Change", "Your email is not associated with any account in our system. Please try again.")



    def login(self):
        self.win.destroy()
        log = login.LoginWindow()
        log.main()
