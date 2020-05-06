from tkinter import *
from tkinter import messagebox

import su
import ou
import vip
import welcome
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cscD@t@Bas3",
    database="TheHive",
    autocommit=True
)

cursor = db.cursor()


class LoginWindow:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.userLabel = Label(self.canvas, text="Enter Username", font='Arial 20 bold', bg='#454b54',
                               fg='#f7cc35')
        self.username = Entry(self.canvas, font='Arial 20 bold', bg='white')

        self.passLabel = Label(self.canvas, text="Enter Password", font='Arial 20 bold', bg='#454b54',
                               fg='#f7cc35')
        self.password = Entry(self.canvas, show='*', font='Arial 20 bold', bg='white')

        self.backButton = Button(self.canvas, text="Back", font='Arial 20 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.welcome)
        self.logButton = Button(self.canvas, text="Login", font='Arial 20 bold', bg='#454b54', fg='#f7cc35',
                                command=lambda: self.log_btn())

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.userLabel.pack(expand=TRUE)
        self.username.pack(expand=TRUE)

        self.passLabel.pack(expand=TRUE)
        self.password.pack(expand=TRUE)

        self.backButton.pack(expand=TRUE)
        self.logButton.pack(expand=TRUE)

        self.win.mainloop()

    def ou(self):
        self.win.destroy()
        ordUser = ou.main()
        ordUser.main()

    def vip(self):
        self.win.destroy()
        vipUser = vip.main()
        vipUser.main()

    def su(self):
        self.win.destroy()
        superUser = su.main()
        superUser.main()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()

    def log_btn(self):
        username = self.username.get()
        password = self.password.get()

        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()

        if account:
            #set user status to ON and all other users to NULL
            #Keep track of which user is logged in on this devide
            cursor.execute("Update users set status = NULL")
            cursor.execute("UPDATE users SET status = 'ON' where username = '%s'" %username)

            #Direct to user page based on type
            cursor.execute("SELECT user_type FROM users WHERE username = '%s'" % username)
            acct_type = cursor.fetchone()[0]
            if acct_type == "OU":
                cursor.close()
                self.ou()
            elif acct_type == "VIP":
                self.vip()
            elif acct_type == "SU":
                cursor.close()
                self.su()
        elif username == "" or password == "":
            messagebox.showwarning("Login Status", "All fields are required!")
        else:
            messagebox.showerror("Login Status", "Account does not exist!")
